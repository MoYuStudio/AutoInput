
# = COPYRIGHT © 2020 MOYU STUDIO. ALL RIGHTS RESERVED. = #

import time
import win32gui

print('')
print('= MoYuStudio AutoInput Tool =')
print('COPYRIGHT © 2020 MOYU STUDIO. ALL RIGHTS RESERVED.')
print('')

for i in range(35):
    window_hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(window_hwnd)

    print('')
    print('捕获当前窗口 The Window u Focusing Now is ...'+'['+str(i)+']')
    print('句柄 ID for the PC ：'+str(window_hwnd))
    print('标题 Title for this Window：'+str(window_title))

    time.sleep(1)

# = COPYRIGHT © 2020 MOYU STUDIO. ALL RIGHTS RESERVED. = #
