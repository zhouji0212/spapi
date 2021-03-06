#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 0011 14:31
# @Author  : Hadrianl 
# @File    : util.py
# @License : (C) Copyright 2013-2017, 凯瑞投资



RET_CODE_MSG_UNINIT = {0: '代表成功',
                       -1:  '用户未登出',
                       -2: '释放异常'}

RET_CODE_MSG_LOGIN_STATUS = {1: '没有登入',
                             2: '连接中',
                             3: '已连接',
                             4: '连接失败',
                             5: '已登出',
                             6:'API阻塞'}

RET_CODE_MSG_ORDER = {0: '表示成功',
                      -1: '用户未登入',
                      -2: '无记录',
                      -3: '价格输入有误',
                      -4: '止损/限价,触发价格不正确',
                      -5: '增强止损,止损价格不正确',
                      -6: '增强止损,追踪市场价格不正确',
                      -7: '双向限价,止损价格不正确',
                      -8: '开仓/平仓,触发价格不正确',
                      -9: '开仓/平仓,止赚价格不正确',
                      -10: '开仓/平仓,止损价格不正确'}

RET_CODE_MSG_CHANGE_ORDER = {0: '成功',
                             -1: '用户未登入',
                             -2: '无记录',
                             -3: '价格输入有误'}

RET_CODE_MSG_REQFUNC = {0: '请求成功',
                        -1: '登入时 UserID 不一致或此 UserID 未登入',
                        -2: 'AE Mode 时未 AccountLogin Client,取得 AccInfo 信息为空',
                        -3: '获取数据不存在或空',
                        -5: 'DLL 异常'}

ORDER_STOPTYPE = {0: '非止损/非限价触发',
                  'L': '限价止损',
                  'U': '升市触发',
                  'D': '跌市触发'}

ORDER_ORDERTYPE = {0: '限价指令类型',
                   2: '竞价指令类型 ',
                   6: '市场价指令类型'}

ORDER_CONDTYPE = {0: '普通指令',
                  1: '止损指令',
                  3: '指定时间发送指令',
                  4: '双向限价指令',
                  6: '追踪止损指令 '}

ORDER_VALIDTYPE = {0: '当天有效',
                  1: '成交并取消',
                  2: '成交或取消',
                  3: '直到有效期',
                  4: '直到自定时间'}

ORDER_STATUS = {0: '发送中',
                1: '工作中',
                2: '无效',
                3: '待定',
                4: '新增中',
                5: '更改中',
                6: '删除中',
                7: '无效中',
                8: '部分成交且工作中',
                9: '已成交',
                10: '已删除',
                18: '等待批准',
                20: '成交已覆盘',
                21: '删除已覆盘',
                24: '同步异常中',
                28: '部分成交已删除',
                29: '部分成交并删除已覆盘 ',
                30: '交易所無效',
                }

HOST_TYPE = {80: '交易连接',
             81: '交易连接',
             83: '一般价格连接',
             88: '一般资讯连接'}

HOST_CON_STATUS = {1: '连接中',
                   2: '已连接',
                   3: '连接错误',
                   4: '连接失败'}

ACTION = {1: '新增指令',
          2: '更改指令',
          3: '删除指令'}

MARGIN_PERIOD = {-2: '错误',
                 -1: '混合',
                 0: 'NULL',
                 1: '隔夜',
                 2: '即日',
                 3: '段落暂停'}