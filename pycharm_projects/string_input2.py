print("""
**************************
            英雄联盟
*************************""")
role = input('请输入角色：')
equipment = input('请输入拥有的装备：')
upgrade_equipment = input("请输入想购买的装备：")
pay = input('输入付款金额：')
equipment = upgrade_equipment
print('{}拥有{}装备，购买此装备花了{}钱。'.format(role,equipment,pay))