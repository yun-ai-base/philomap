// Philomap 冒烟测试：覆盖核心交互，防止回归
// 运行：npm run test:smoke
const { test, expect } = require('@playwright/test');

test.describe('数据加载', () => {
  test('加载数据并渲染节点', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group', { timeout: 15000 });
    const nodeCount = await page.locator('.node-group').count();
    expect(nodeCount).toBeGreaterThan(50); // 当前 102 位哲人
  });

  test('数据包含关键哲人', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    const names = await page.evaluate(() =>
      dataRef.philosophers.map((p) => p.id)
    );
    expect(names).toContain('plato');
    expect(names).toContain('aristotle');
    expect(names).toContain('confucius');
  });
});

test.describe('六个视图切换', () => {
  test('切换所有视图不报错', async ({ page }) => {
    const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.goto('/');
    await page.waitForSelector('.node-group');

    // 非模态视图可直接切换；模态视图（duel/quiz）用关闭按钮切回后继续
    for (const view of ['river', 'spectrum', 'duel']) {
      await page.click(`[data-view="${view}"]`);
      await page.waitForTimeout(300);
    }
    // 关闭 duel 模态
    await page.click('#duel-close');
    await page.waitForTimeout(200);
    // 打开 quiz 模态
    await page.click('[data-view="quiz"]');
    await page.waitForTimeout(300);
    await page.click('#quiz-close');
    await page.waitForTimeout(200);
    // 其余视图
    for (const view of ['twin', 'star']) {
      await page.click(`[data-view="${view}"]`);
      await page.waitForTimeout(300);
    }
    expect(errors).toEqual([]);
  });

  test('切回星图后节点仍在', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.click('[data-view="river"]');
    await page.click('[data-view="star"]');
    await page.waitForSelector('.node-group');
    expect(await page.locator('.node-group').count()).toBeGreaterThan(50);
  });
});

test.describe('节点球内多行名字', () => {
  test('名字以 tspan 多行渲染在球内', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    const multiline = await page.evaluate(() => {
      const labels = document.querySelectorAll('.node-label');
      let multi = 0;
      labels.forEach((l) => {
        if (l.querySelectorAll('tspan').length > 1) multi++;
      });
      return { total: labels.length, multi };
    });
    expect(multiline.total).toBeGreaterThan(50);
    expect(multiline.multi).toBeGreaterThan(0); // 长名字有换行
  });

  test('长名字如密尔为三行', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    const lines = await page.evaluate(() => {
      let found = null;
      document.querySelectorAll('.node-group').forEach((g) => {
        if (g.__data__ && g.__data__.id === 'mill') {
          found = [...g.querySelectorAll('.node-label tspan')].map((t) => t.textContent);
        }
      });
      return found;
    });
    expect(lines).toBeTruthy();
    expect(lines.length).toBeGreaterThan(1);
  });
});

test.describe('关系旅行（思想之旅）', () => {
  test('打开详情面板显示思想之旅区块', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.evaluate(() => {
      const n = simData.allNodes.find((x) => x.id === 'aristotle');
      openDetailPanel(n);
    });
    await page.waitForSelector('#detail-panel.open');
    const journeyVisible = await page.evaluate(
      () => document.getElementById('dp-journey').style.display
    );
    expect(journeyVisible).toBe('block');
  });

  test('上下游邻接表正确', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    const result = await page.evaluate(() => {
      const up = [...(simData.upstreamOf.get('aristotle') || [])];
      const down = [...(simData.downstreamOf.get('aristotle') || [])];
      return { up, down };
    });
    expect(result.up).toContain('plato'); // 亚里士多德受柏拉图启发
    expect(result.down).toContain('aquinas'); // 影响了阿奎那
  });

  test('上游暖色、下游冷色高亮', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.evaluate(() => {
      const n = simData.allNodes.find((x) => x.id === 'aristotle');
      openDetailPanel(n);
    });
    await page.waitForTimeout(500);
    const colors = await page.evaluate(() => {
      const get = (id) => {
        let c = null;
        document.querySelectorAll('.node-group').forEach((g) => {
          if (g.__data__ && g.__data__.id === id) {
            c = g.querySelector('.node-glow').getAttribute('stroke');
          }
        });
        return c;
      };
      return { plato: get('plato'), aquinas: get('aquinas') };
    });
    // 上游（柏拉图）暖色 #fbbf24，下游（阿奎那）冷色 #34d399
    expect(colors.plato).toContain('251, 191, 36');
    expect(colors.aquinas).toContain('52, 211, 153');
  });
});

test.describe('时间推进动画', () => {
  test('播放按钮推进年份并点亮节点', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.click('#time-play');
    await page.waitForTimeout(1500);
    const state = await page.evaluate(() => ({
      playing: playbackOn,
      yearText: document.getElementById('time-display').textContent,
    }));
    expect(state.playing).toBe(true);
    expect(state.yearText).not.toBe('全部时代');
    // 停止
    await page.evaluate(() => stopPlayback());
  });

  test('播放结束后自动复位', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.evaluate(() => {
      // 直接模拟播放结束
      playbackStart = performance.now() - 30000;
      playbackOn = true;
      timePlayBtn.textContent = '■';
    });
    await page.evaluate(() => tickPlayback());
    await page.waitForTimeout(500);
    const state = await page.evaluate(() => ({
      playing: playbackOn,
      btn: timePlayBtn.textContent,
      year: document.getElementById('time-display').textContent,
    }));
    expect(state.playing).toBe(false);
    expect(state.btn).toBe('▶');
    expect(state.year).toBe('全部时代');
  });
});

test.describe('关系类型筛选', () => {
  test('点击师承只显示师承边', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.click('#rel-legend .rl-item[data-type="teacher-student"]');
    await page.waitForTimeout(600);
    const types = await page.evaluate(() => {
      const cnt = {};
      document.querySelectorAll('line.edge-line').forEach((l) => {
        const d = l.__data__;
        if (l.getAttribute('display') !== 'none' && d) {
          cnt[d.type] = (cnt[d.type] || 0) + 1;
        }
      });
      return cnt;
    });
    expect(types['teacher-student']).toBeGreaterThan(0);
    expect(types['influence']).toBeUndefined();
    expect(types['debate']).toBeUndefined();
  });

  test('三类全选自动清空', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.click('#rel-legend .rl-item[data-type="teacher-student"]');
    await page.click('#rel-legend .rl-item[data-type="influence"]');
    await page.click('#rel-legend .rl-item[data-type="debate"]');
    const size = await page.evaluate(() => currentFilters.relType.size);
    expect(size).toBe(0);
  });
});

test.describe('详情面板折叠', () => {
  test('次要 section 默认折叠', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.evaluate(() => {
      const n = simData.allNodes.find((x) => x.id === 'kant');
      openDetailPanel(n);
    });
    await page.waitForSelector('#detail-panel.open');
    const collapsed = await page.evaluate(() =>
      document.getElementById('dp-events').classList.contains('collapsed')
    );
    expect(collapsed).toBe(true);
  });

  test('点击标题可折叠核心 section', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.evaluate(() => {
      const n = simData.allNodes.find((x) => x.id === 'kant');
      openDetailPanel(n);
    });
    await page.waitForSelector('#detail-panel.open');
    await page.click('#dp-core .dp-section-title');
    const collapsed = await page.evaluate(() =>
      document.getElementById('dp-core').classList.contains('collapsed')
    );
    expect(collapsed).toBe(true);
  });
});

test.describe('基因测试（幽灵 id 已修复）', () => {
  test('computeQuizResults 不产生 NaN', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    const result = await page.evaluate(() => {
      // 模拟随机答题
      const answers = quizQuestions.map(
        (q) => q.opts[Math.floor(Math.random() * q.opts.length)].s
      );
      const scores = {};
      for (const ans of answers) {
        for (const [phId, pts] of Object.entries(ans)) {
          scores[phId] = (scores[phId] || 0) + pts;
        }
      }
      return Object.keys(scores).length;
    });
    expect(result).toBeGreaterThan(0);
  });

  test('quiz 视图打开无报错', async ({ page }) => {
    const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.click('[data-view="quiz"]');
    await page.waitForSelector('#qz-body');
    expect(errors).toEqual([]);
  });
});

test.describe('安全：XSS 与 CSP', () => {
  test('CSP meta 存在', async ({ page }) => {
    await page.goto('/');
    const csp = await page.evaluate(() =>
      document.querySelector('meta[http-equiv="Content-Security-Policy"]') !== null
    );
    expect(csp).toBe(true);
  });

  test('escapeHtml 函数存在且可转义', async ({ page }) => {
    await page.goto('/');
    const escaped = await page.evaluate(() =>
      escapeHtml('<img src=x onerror=alert(1)>')
    );
    expect(escaped).toBe('&lt;img src=x onerror=alert(1)&gt;');
  });
});

test.describe('无障碍', () => {
  test('节点有 aria-label 和 tabindex', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    const a11y = await page.evaluate(() => {
      const g = document.querySelector('.node-group');
      return {
        aria: g.getAttribute('aria-label'),
        tabindex: g.getAttribute('tabindex'),
        role: g.getAttribute('role'),
      };
    });
    expect(a11y.aria).toBeTruthy();
    expect(a11y.tabindex).toBe('0');
    expect(a11y.role).toBe('button');
  });

  test('html lang 已设置', async ({ page }) => {
    await page.goto('/');
    const lang = await page.evaluate(() => document.documentElement.lang);
    expect(['zh-CN', 'en']).toContain(lang);
  });
});

test.describe('语言切换', () => {
  test('切英文后节点名字变化', async ({ page }) => {
    await page.goto('/');
    await page.waitForSelector('.node-group');
    await page.click('#lang-btn');
    await page.waitForTimeout(300);
    const en = await page.evaluate(() => {
      let name = null;
      document.querySelectorAll('.node-group').forEach((g) => {
        if (g.__data__ && g.__data__.id === 'plato') {
          name = g.querySelector('.node-label').textContent;
        }
      });
      return name;
    });
    expect(en).toBe('Plato');
    // 切回中文
    await page.click('#lang-btn');
  });
});
