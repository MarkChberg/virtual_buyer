搜索中心设计


搜索功能
    man端功能实现：
        可以添加spu信息

        添加属性与属性值

        可以给spu信息绑定sku信息（绑定库存，属性）


    搜索功能实现：
        属性搜索
            根据不同属性交叉搜索商品



Spu： id name produce_year class_id_one（FK） class_id_two(FK) create_time update_time

ClassOne: id class_name class_desc

ClassTwo: id class_name class_one_id(FK) class_desc

Attr: id attr_name

Value: id attr_id(FK) value_name

Attr_link_Value: id attr_id(FK) value_id(FK) sku_id(FK)

Sku: id spu_id(FK) ware_address stocks price create_time update_time



