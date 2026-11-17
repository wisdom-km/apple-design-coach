# Design record

示例文件，演示项目里已经确认的视觉记录。不是某个真实用户的产品。

- status: confirmed
- surface: android-phone
- direction_name: 系统密表
- confirmed_by: user
- visual_record_note: 色和字以本文件为准。平台范围见同目录 context.md，不在这里重写。

## Color roles

- 背景：#f4f7f5（项目决定）
- 主操作：#0f6e56（项目决定，不是 Material 色板原文）
- 危险：文字色，不使用主操作的填充

## Type

- 系统无衬线
- 金额是唯一的大字
- 正文约 16px

## Density

- 单任务，无 3–5 项目的地底栏
- 行列表，不做等权卡片

## Components

- 顶栏标题 + 溢出菜单里的设置
- 主按钮「保存」
- 「删除」与主按钮不同形

## Placement

- 设置不占主路径
- 长标题换行，不截成省略号

## Unknown

- 删除是先确认还是可撤销：还没定

## Custom

- receipt-photo: optional-never-required

后来的人更新本文件时保留 `receipt-photo` 这一行。不要因为模板里没有它就删掉。
