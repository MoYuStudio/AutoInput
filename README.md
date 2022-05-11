# AutoInput 自动输入

>设定键盘执行计划当窗口聚焦时执行

## 开始使用

>在'data'文件夹中有'config'&'setting'两个文件

### Setting 设置
>您可以使用 记事本 等 文件读取软件 打开 以修改

>默认设置为
>F2 关闭 程序
>60 秒 执行一次
>True 开机自启 为打开

>打开后您会看到
```
{\
'close_key':'F2',		# 关闭程序 快捷键
'sleep_time':'60',		# 执行间隔 单位秒 注意：标准执行为1秒，但是会受到您的计算机运行效率的影响，实际可能会有出入
'set_autostartcmd':'True',	# 开机自启 True or False 是True 或 否False   注意：只能填入 True 或 False
}
```
### Config 配置
>您可以使用 记事本 等 文件读取软件 打开 以修改

>我们给您预先准备了两个配置 分别为 Microsoft Office Word 与 Microsoft Office PowerPoint
>该配置会为您定时使用快捷键 Ctrl + S 进行保存

>打开后您会看到

```
{\
0:{\				# 自动执行进程序号
'name' : 'Word',		# 进程名字
	'key_type':'hotkey',	# 按键类型 key or hotkey 单个按键key 或 快捷键hotkey   注意：只能填入 key 或 hotkey
	'key' : '',		# 单个按键key
	'hotkey':['ctrl','s']	# 快捷键hotkey
	},
1:{\				# 自动执行进程序号 每个依序加一
'name' : 'PowerPoint',
	'key_type':'hotkey',
	'key' : '',
	'hotkey':['ctrl','s']
	},
}
```
##### 配置样板
>使用时 自动执行进程序号 依序加一
>填写 进程名字 按键类型 及 该按键类型 的 单个按键key 或 快捷键hotkey
>注意：如果为空进程会无法运行
```
0:{\
'name' : '',
	'key_type':'',
	'key' : '',
	'hotkey':['','']
	},
```
