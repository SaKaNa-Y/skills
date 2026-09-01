# Antfu “The Progressive Path” 第一方资料研究

> 研究日期：2026-09-01
>
> 范围：完整核对 Anthony Fu（Antfu）本人网站、`antfu/talks` 官方仓库中的两版幻灯片与 speaker notes，以及 Antfu 本人索引所链接的两个大会录播。本文不设计或实现新 skill；最后只判断当前设想与演讲的对应关系。

## 结论先行

用户的理解**方向上成立，但需要改写得更准确**。

Antfu 的“平衡点”不是一套比较 React、Vue、某个库 A、库 B 的通用评分表，而是一个站在使用者一侧的采用启发式：一边是**学习和使用工具的成本**，另一边是**自己完成同一件事的成本**；前者应显著低于后者，工具才更可能值得采用。他同时把工具定义为让事情变得更快和／或更容易，并明确说“好”是相对于目标而言的，项目最终是否成功不能在社区验证之前确定。[原版 speaker notes：工具定义与平衡](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L120-L203)

演讲所谓的“工具构成”也需要纠正：Antfu 分解的不是工具的软件架构，而是 **Cost of Using a Tool（使用外部工具的成本）**，包括：

1. **发现成本**：人们是否容易意识到这里需要一个工具；工具能否用一两句话讲清用途、容易被找到。
2. **学习成本**：是否容易理解、上手，多久能开始受益。
3. **价格**：工具本身的金钱成本；开源通常免费，但免费不等于无成本。
4. **采用成本**：安装与集成、扩展性、未来需求以及迁移成本。

[原版 speaker notes：成本分解](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L208-L262)

因此，新 skill 可以合理地做成：**先分析当前仓库和具体工作，再有边界地搜索真实候选工具，以当前方案／自己实现为基线比较总成本与收益，并给出可共存、可回退、分阶段的采用路径。** 但“自动搜索有没有更好的工具并排名”并不是演讲原意；仓库分析、候选搜索、生态健康、安全、许可证、性能、长期维护、锁定风险和最终推荐规则都需要作为独立设计补上。

最重要的命名与行为护栏是：它寻找的应该是 **fit（适配度）**，不是脱离上下文的 “best（最好）”。合法结果必须包括“保留现有工具”或“证据不足，不建议更换”。

## 证据标签

- **[原意]**：幻灯片或 speaker notes 直接表达。
- **[释义]**：对 Antfu 的图示、案例或结论作忠实重述。
- **[延伸]**：适用于拟议 skill 的设计推论，不能归因于 Antfu。

## 官方材料与版本覆盖

Antfu 的 [Talks 索引](https://antfu.me/talks) 将它正式列为 **“Anthony's Road to Open Source — Part 2: The Progressive Path”**，摘要是渐进式方法如何帮助构建更好的开源项目，以及为什么社区需要接纳这种方法。索引列出三次发表：

| 日期 / 场合 | 第一方材料 | 录像 | 本次核对结果 |
| --- | --- | --- | --- |
| 2024-02-29 Vue Amsterdam | [Antfu 文章页](https://antfu.me/posts/roads-to-oss-progressive-vueams-2024) · [完整 slide source + speaker notes](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md) · [在线幻灯片](https://talks.antfu.me/2024/vue-amsterdam/overview) | [Vuejs Amsterdam 官方录播，26:48](https://www.youtube.com/watch?v=67Pha7sZ6l0) | 当前能确认的最早完整版本；包含全部核心模型和 Vue、Nuxt、Vite 案例。 |
| 2024-06-01 Frontend Nation | Antfu 索引没有单独的 slide source，现场使用的是同一核心讲稿 | [Vue School / Frontend Nation 录播，27:35](https://www.youtube.com/watch?v=YbyXsi4TPtc) | 用于逐段视觉核对与时间锚点；内容与 2 月版本一致。 |
| 2024-10-03 ViteConf | [ViteConf 版 slide source + speaker notes](https://github.com/antfu/talks/blob/main/2024-10-03/src/slides.md) · [PDF](https://github.com/antfu/talks/blob/main/2024-10-03/2024-10-03-viteconf-en.pdf) · [仓库说明](https://github.com/antfu/talks/blob/main/2024-10-03/README.md) | Antfu 索引未提供独立 Watch 链接 | 保留整个核心模型；新增 Nuxt 3→4 和 Vite 5→6.0→6.1 的渐进迁移案例。 |

两版 speaker notes 对“工具”“平衡”“成本分解”和四类 progressive path 的表述没有实质变化。ViteConf 版主要更新身份信息、删减部分早期例子，并增加当时正在发生的版本迁移案例。[ViteConf 版：Nuxt 4 路径](https://github.com/antfu/talks/blob/main/2024-10-03/src/slides.md#L833-L910)；[ViteConf 版：Vite 6 路径](https://github.com/antfu/talks/blob/main/2024-10-03/src/slides.md#L912-L986)

### 录像时间锚点

两个录播都没有可导出的 YouTube 字幕轨，也没有发布者章节。以下锚点通过 Vue Amsterdam 录播画面、画面内嵌字幕和官方 speaker notes 逐页对齐，适合导航，不应作为发布者逐字稿：

- [`02:53`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=173s)：工具的定义——更快和／或更容易。
- [`04:53`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=293s)：出现天平；约 `05:02` 明确学习／使用工具的成本 vs 自己完成的成本。
- [`06:28`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=388s)：开始分解使用工具的成本；发现约 `06:42`、学习约 `07:02`、价格约 `07:25`、采用约 `07:53`。
- [`08:47`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=527s)：楼层与楼梯；progressive 的定义。
- [约 `10:00`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=600s)：Vue 的渐进集成。
- [`12:52`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=772s)：Nuxt 的渐进 onboarding 与按需功能，持续至约 `19:07`。
- [`19:07`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=1147s)：Vite 的版本与生态兼容。
- [`21:29`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=1289s)：渐进 breaking changes。
- [`24:43`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=1483s)：coexistence 与 migration middle stages。
- [`25:00`](https://www.youtube.com/watch?v=67Pha7sZ6l0&t=1500s)：四类路径回顾；约 `26:34` 以 “Divide and Conquer” 收束。

## 演讲的完整论证结构

### 1. 先定义工具，而不是先列产品

**[原意]** 工具至少应让用户把事情做得更快或更容易。Antfu 随即否定了脱离预期判断“好工具”的可能性：一个只解决作者自己问题的工具也完全可以是好工具；如果目标变成让更多人受益，问题才转为怎样构建 general and useful 的工具。[工具定义、相对目标与社区验证](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L120-L203)

**[释义]** “是否适合”必须先有使用者、工作和预期；星数、功能数量或流行度不能单独回答。

### 2. 平衡点：采用成本与自行完成成本

**[原意]** 使用者会权衡成本与收益。Antfu 放到天平上的两个主要因素是：

- Cost of learning and using the tool；
- Cost of doing something oneself。

他的预评估公式是：前者应当 **much less than** 后者。十个数字求和不值得先找库；复杂微积分则很可能值得；但若库要求先掌握一百项配置，使用者又会继续寻找更容易的方案。[天平与例子](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L175-L203)

**[释义]** 这里不是要求两边相等，而是要求工具成本被它带来的收益充分覆盖。所谓 balance 是权衡关系，不是“50/50 的平衡”。

### 3. 分解的是使用成本，不是工具内部结构

**[原意]** 使用工具的成本由发现、学习、价格和采用构成。采用成本明确包含安装、集成、扩展以及迁移。Antfu 还提醒：复杂性可能从一个地方转移到另一个地方，但不会神奇消失；面对复杂问题，工具很难完全没有复杂性。[成本四项及复杂性边界](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L208-L262)

**[释义]** 目标不是把候选工具的 API 数量压到最少，而是让用户只在需要时承担相称的复杂度。

### 4. Progressive：用楼梯替代一次跳跃

**[原意]** Antfu 用从一楼到二楼的图解释 progressive：如果只能一次跳过高墙，很多人会放弃；楼梯把困难目标拆成多个更小的步骤。他把 progressive 解释为让事情更容易接近的“楼梯”。[楼梯定义](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L264-L315)

### 5. Vue：渐进集成

**[原意]** Vue 可以从无构建工具的 CDN、Web Components，逐步走到 SPA、SSG、SSR、原生目标与 Vapor。这些层级覆盖不同场景，能和其他技术共存，也允许大型旧代码库只迁移一部分。[Vue 集成层级](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L317-L407)

**[释义]** 采用不必等于全仓替换；候选工具能否从一个边界清楚的小范围开始，是实际的 fit 信号。

### 6. Nuxt：渐进 onboarding 与渐进功能

**[原意]** Nuxt 用极小起始界面降低初始知识要求，再让用户通过文件约定、模块生态、DevTools 和教程逐步发现路由、部署、服务端 API、TypeScript、PWA、SEO、i18n 等能力；没有使用的功能无需预先学习。[Nuxt onboarding](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L409-L479)；[Nuxt features](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L481-L648)

**[释义]** 功能丰富和初始复杂并非同一件事。好的渐进工具可以强大，但初始暴露面小、后续能力可发现、按需启用。

### 7. Vite：渐进 breaking changes

**[原意]** Antfu 把 forward compatibility 与 backward compatibility 作为降低破坏性迁移成本的两条路径：提前用 experimental / future flags 在当前版选择未来行为；或先弃用和警告、以后再删除，并提供兼容层。根本目标是允许 legacy 与 new 共存，为迁移提供可停留的 “middle stages”。[Vite 与两类兼容路径](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L650-L845)

ViteConf 版把这套思想落到两个当时的新案例：Nuxt 3 可以提前选择 Nuxt 4 行为，Nuxt 4 仍可退回旧行为；Vite 6.0 先承载大规模内部重构但尽量保持用户层平坦升级，到 6.1 再推动 Environment API。[Nuxt 4 案例](https://github.com/antfu/talks/blob/main/2024-10-03/src/slides.md#L833-L910)；[Vite 6 案例](https://github.com/antfu/talks/blob/main/2024-10-03/src/slides.md#L912-L986)

### 8. 总结：把大目标交还给用户分而治之

**[原意]** 演讲最终归纳四类 progressive path：

- onboarding：容易理解和开始；
- integrations：适应不同场景、容易采用；
- features：从最小能力开始，随用户成长；
- breaking changes：提供迁移的中间阶段。

结论是：提供 progressive paths，就是让用户能够对自己的目标 “Divide and Conquer”。[完整回顾与结语](https://github.com/antfu/talks/blob/main/2024-02-29/src/slides.md#L847-L929)

## 对拟议 skill 的事实性判断

### 演讲直接支持的部分

1. **必须有基线**：候选工具要与当前方案／自行完成同一工作的成本比较，而不是彼此孤立评分。
2. **适配是相对的**：先确定仓库的真实工作、使用者、预期和约束，再谈“好”。
3. **采用成本不止安装命令**：学习、集成、扩展、迁移和价格都属于决策。
4. **采用路径本身是选择标准**：能否局部引入、与现有技术共存、按需启用、渐进迁移和回退，影响工具是否适合。
5. **工具应降低真实工作总成本**：只增加抽象或配置、却没有覆盖其成本，不满足演讲中的价值关系。

### 合理但必须标成独立延伸的部分

下列能力是一个可靠的“仓库工具选择” skill 所必需，但 Antfu 没有在这场演讲中提出：

- **[延伸] 仓库分析**：识别当前技术栈、架构边界、已用工具、重复实现、性能／质量痛点、团队约束。
- **[延伸] 有边界的候选搜索**：搜索官方文档、源代码、发布记录和真实兼容证据，并设候选数量和停止条件。
- **[延伸] 工程适配维度**：运行时和平台兼容、许可证、安全记录、维护活跃度、治理与 bus factor、性能、包体积、稳定性、生态成熟度、供应链风险、长期维护和锁定成本。
- **[延伸] 证据门槛**：不能因功能表或流行度直接推荐；需要与 Anchor Repository 双向可验证的适配证据。
- **[延伸] 推荐处置**：至少允许 `Keep Current`、`Trial`、`Recommend`、`Needs Evidence`、`Reject`，避免强制迁移。
- **[延伸] 用户决策点**：搜索和分析是只读的；真正修改依赖、框架迁移或重构需要用户另行授权。

### 不应归因于这场演讲的说法

- “Antfu 提出了一套框架／库选型方法。”没有；他讨论的是如何构建和采用渐进工具。
- “工具越通用、功能越多越好。”没有；good 相对于预期，复杂度也不会消失。
- “AI 应在每个仓库里主动找替代品。”没有；演讲没有讨论 AI、仓库审计或自动搜索。
- “四项成本足以完成工程选型。”不够；它们没有显式覆盖安全、许可证、项目治理、运行时性能和长期运营风险。
- “把每个候选打成一个数字就能找到平衡点。”没有；演讲给的是启发式关系，不是权重或总分公式。
- “发现成本就是 AI 搜索候选所花的时间。”不准确；Antfu 指用户是否容易意识到需要工具、是否容易理解和找到它。AI 搜索可以降低人的发现成本，但这是二次应用。

## 对 skill 边界的建议性推论

**[延伸]** 若后续把想法写成 skill，最忠于演讲又适合现有仓库的最小闭环是：

1. 确认具体 Tool Decision：要改善哪项现有工作，为什么现在需要选择。
2. 建立 Current Baseline：当前工具／自行实现、真实痛点、必要约束和转换成本。
3. 有界搜索真实候选；允许搜索结果为空。
4. 对每个候选分别记录收益、发现／学习／价格／采用成本，以及独立补充的工程风险。
5. 检查 Progressive Fit：小范围试用、共存、按需能力、中间迁移阶段、回退路径。
6. 给出证据化处置和最小可证伪试验；由用户决定是否进入实现。

这与仓库现有的 `set-theory-for-projects` 不同：后者依据 Part I 寻找 Anchor Project 的 Universal Core、Adapter 或 Platform 扩展机会；拟议 skill 是为一个具体仓库问题寻找和判断外部工具。两者都应显式、只读、有界，但不应合并成一个工作流。[现有跨项目发现 ADR](../adr/0002-cross-project-discovery-is-explicit-and-bounded.md)

## 后续讨论最值得先定的事实边界

以下不是 Antfu 的原话，而是命名和设计 skill 前需要由用户决定的问题：

1. skill 的主任务是“在已经存在选型问题时比较候选”，还是“主动审计仓库并发现潜在工具机会”？后者范围更大、误报风险更高。
2. 是否把框架迁移、局部库选择、开发工具、托管服务都放在同一 skill？这些决策的证据和风险尺度差异很大。
3. “更好”的默认基线是什么：当前工具、内部实现、完全不用工具，还是用户已经给出的候选？
4. 哪些维度属于硬门槛，哪些只是权衡项？例如许可证和运行时不兼容通常应直接淘汰，而不是被星数抵消。
5. 输出停在哪里：只到研究与推荐，还是还要给渐进试验方案？演讲强烈支持后者，但不支持自动实施。
6. 是否明确接受 No-change Result？若不接受，skill 会被结构性地推向“为了更换而更换”。

## 研究局限

- 两个官方 YouTube 录播都没有可导出的字幕轨或发布者章节；精确陈述优先引用 Antfu 官方 speaker notes，时间戳仅用于导航。
- Frontend Nation 没有独立的官方 slide source 目录；其录像内容与 2024-02-29 版本逐段一致，但本文没有声称像素级完全相同。
- 本文没有独立复算 Vite、Vue、Nuxt 的兼容性历史或用户迁移成功率；案例结论均保留为 Antfu 的演讲叙述。
- 演讲讨论的是 2024 年的工具设计经验，不能代替 2026 年具体候选工具的实时研究。
