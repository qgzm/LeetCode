# 使用者：姜海波
# 创建时间：2023/3/5  23:45
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ans=-1
        maxProfit = totalProfit = operations = customersCount = 0
        for i in customers:
            operations+=1
            customersCount+=i
            curCustomers=min(customersCount,4)
            customersCount-=curCustomers
            totalProfit+=boardingCost*curCustomers-runningCost
            if totalProfit>maxProfit:
                maxProfit=totalProfit
                ans=operations
        # 客户为零
        if customersCount==0:
            return ans
        profitEachTime=boardingCost*4-runningCost
        # 满载的时候每趟的利润都小于零的话
        if profitEachTime<=0:
            return ans
        # 客人多于零且每趟最大利润大于零
        if customersCount>0:
            fullTimes=customersCount//4
            totalProfit+=profitEachTime*fullTimes
            operations+=fullTimes
            if totalProfit>maxProfit:
                maxProfit=totalProfit
                ans=operations
            remainingCustomers=customersCount%4
            remainingProfit=boardingCost*remainingCustomers-runningCost
            totalProfit+=remainingProfit
            if totalProfit>maxProfit:
                operations+=1
                ans+=1
        return ans
