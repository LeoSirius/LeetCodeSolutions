## 思路1 利用一个buff_dict

设`a + b = target`利用一个字典，key存放a或b其中一个，value则是key在原数组中的索引。依次遍历数组，当第一次遇到a或b时，把他们放入`dict`，第二次遇到a或b时，直接返回即可。