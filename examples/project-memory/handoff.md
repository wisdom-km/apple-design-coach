# 实现交接（示例）

这一份只在用户说「交给写代码的 AI」时才写。只讨论方向时不写它。

示例数据。不是一份真实产品的开发规格，也不指定技术栈。

- 表面：android-phone。平台范围见 [context.md](context.md)。
- 视觉记录：[DESIGN.md](DESIGN.md)。颜色角色、字号、密度、组件和 `receipt-photo: optional-never-required` 以那份文件为准。这里不另写色值，也不另建一份记录。
- 保留字段：`receipt-photo: optional-never-required`。更新设计记录时这一行留着。

## 组件与交互

- 主操作是填充按钮。危险操作是文字，不与主按钮同形。角色见 DESIGN.md。
- 列表读失败时可以重试。空白时可以去记第一笔。
- 记一笔的主路径不申请相机、相册或通讯录。
- 用户点了附收据照片并且被拒绝时：可以再试一次，也可以保存这笔且不附照片。拒绝不挡住保存。
- 删除是先确认还是可撤销：未知，见 DESIGN.md 的 Unknown。实现删除前要问。这里不补一个答案。

## 状态

- 已画：账单列表的有记录、空白、加载、失败与重试。见 [android-ledger-list.html](../drafts/android-ledger-list.html)。
- 已画：失败态在窄窗口里放到 150%。见 [android-ledger-list-scaled.html](../drafts/android-ledger-list-scaled.html)。这不是动态字体测试。
- 已画：可选照片被拒绝后的降级。见 [android-ledger-photo-denied.html](../drafts/android-ledger-photo-denied.html)。
- 不适用：记一笔主屏的权限页。见 [android-ledger-after.html](../drafts/android-ledger-after.html)。原因是保存不依赖照片。
- 不适用：单独的离线页。示例是本机列表。
- 尚未核对：删除的确认或撤销。原因是设计记录把它留在 Unknown。

## 主路径

打开账单，看到一条记录或空白，再记一笔，保存。设置在顶栏溢出里，不占主路径。理由是 Purpose：先把这笔看清并记下；Simplicity：不把设置放进主按钮。

## 验收

- 长标题「2026年11月家庭水电燃气合缴账单（含滞纳金说明）」在列表里整句换行，不截成省略号。
- 失败态看得到「重试」，空白态看得到「记第一笔」。
- 保存与删除不同形。
- 不申请权限也能保存。
- 照片被拒绝时，仍有「保存这笔，不附照片」。
- `receipt-photo` 仍是 optional-never-required。

## 数值与资源

官方触控尺寸只用来源表里已有的 Android 48 dp 这一类数字，不在这里新编。项目自己的颜色和「正文约 16px」只写在 DESIGN.md。没有的保持未知。

字体用系统无衬线。仓库里没有附带字体文件，也没有图片附件。不要编一个不存在的素材包。

不要：指定 Kotlin、Flutter、React 或其他框架；借这份交接开始写产品代码；覆盖 DESIGN.md 里用户改过的句子。
