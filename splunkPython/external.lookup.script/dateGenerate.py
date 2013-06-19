'''
Created on 2013-6-7

@author: Asus
'''
import inputdata_download
import inputdata_good_access
import inputdata_play
import inputdata_pv_access
import inputdata_play_order
import inputdata_unorder
import inputdata_RecomendOrder

if __name__ == '__main__':
  # HOST,PORT,SOURCETYPE="10.206.10.31",9990,"good_access"
  # HOST,PORT,SOURCETYPE="10.206.10.31",9991,"play"
  # HOST, PORT, SOURCETYPE = "10.206.10.31", 9992, "pv_access"
  # HOST, PORT, SOURCETYPE = "10.206.10.31", 9993, "order"
  # HOST, PORT, SOURCETYPE = "10.206.10.31", 9994, "play_order"
  # HOST, PORT, SOURCETYPE = "10.206.10.31", 9995, "download"
  # HOST, PORT, SOURCETYPE = "10.206.10.31", 9999, "unorder"
  # HOST, PORT, SOURCETYPE = "10.206.10.31", 10000, "RecommendOrder
    map={'host':'10.206.10.31','year':'2013','month':'06','et_day':13,'lt_day':15,'count':100,'path':'C:\\Users\\Asus\\Desktop\\testData\\'}    
    inputdata_download.run(map,PORT=9995)
    inputdata_good_access.run(map,PORT=9990)
    inputdata_play.run(map,PORT=9991)
    inputdata_pv_access.run(map,PORT=9992)
    inputdata_play_order.run(map,PORT=9994)
    inputdata_unorder.run(map,PORT=9999)
    inputdata_RecomendOrder.run(map,PORT=10000)
   