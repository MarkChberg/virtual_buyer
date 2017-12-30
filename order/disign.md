订单中心设计

实现功能：
    提交订单功能：
        验证商品是否可用
            保存订单到数据库
            生成展示给用户的订单信息，根据商家分成多张子订单
    提交订单功能2：
        要求用户选择已有地址，或者生成新的收获地址
            更新订单信息
            更新订单到待支付
    支付功能
        根据用户信息获取所有的待支付订单
            让用户选择哪几张订单需要支付
            计算总价格，请求支付中心接口，支付中心会记录下用户的购买信息
            返回支付中心的生成url，前台自动跳转
    退款功能
        用户对某一个订单（order_id）提起退款申请
            验证是否存在可退，金额是否无误
            更新订单状态到退款中
            请求支付中心refund接口
            返回true和false
    提供给支付中心的接口：
        需要提供一个更改订单状态的方法，当支付成功时，支付中心会更改订单状态

    购物车功能
        添加到购物车，如果登录放置到session中，并放置到数据库中，如果没有，放置到cookie中
        删除购物车商品功能
        合并购物车功，保持db、cookie、session中对数据一致

    man端：
        显示所有订单，有排序功能

        对订单进行增删改查操作

        可以删选出所有超时订单,一键清空

Models:

order: id order_id user_id(FK) order_status(default 0 : new order 1: ready_pay 2:pay
3：refunding 4:pay_success 5:pay_fail 6:refund_success 7 refund_fail) price create_time update_time

order_item: id order_id(FK) sku_id(FK) price create_time update_time

shopping_cart: id user_id(FK) sku_id(FK) number price create_time update_time



