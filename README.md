# AutoInput 自动输入

>设定键盘执行计划当窗口聚焦时执行

## 开始使用

>在'data'文件夹中有'config'&'setting'两个文件

### config 配置文件
>您可以使用 记事本 等 文件读取软件 打开 以修改
>我们给您预先准备了两个配置 分别为 Microsoft Office Word 与 Microsoft Office PowerPoint
>该配置会为您定时使用快捷键 Ctrl + S 进行保存

```
{\
0:{\				# 自动执行进程序号
'name' : 'Word',		# 进程名字
	'key_type':'hotkey',	# 按键类型 key or hotkey 单个按键key 或 快捷键hotkey
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
>如果为空进程会无法运行
```
0:{\
'name' : '',
	'key_type':'',
	'key' : '',
	'hotkey':['','']
	},
```
