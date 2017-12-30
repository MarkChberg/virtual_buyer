用户与权限模块基本功能实现


用户：
    用户登录功能
        通过账号和密码进行用户的验证

        登录成功后，在cookie中保存用户使用名

    用户注册功能
        根据数据库对应创建前台表单，提交数据，创建新用户
            对提交表单数据进行验证
            对某些不可重复对字段进行ajax请求进行验证

权限
    man端分页显示用户信息
        有一个按照时间进行排序的功能
        对应有删除用户的功能
    man端能给用户安排除管理员外的任何角色
        不同的角色对应不同的权限（目前只使用两种权限，游客和管理员）
    man端做权限验证
        只有管理员权限的才能登录man端进行操作


Models

User： id username password email telephone nick_name pay_password(支付密码，pay模块使用，本模块不显示) role_id create_time update_time

Role：id role_name create_time update_time

Auth: id auth_url create_time update_time(暂且不用，后期权限拓展)

Role_link_Auth: id role_id auth_id create_time update_time（暂且不用，后期权限拓展）
