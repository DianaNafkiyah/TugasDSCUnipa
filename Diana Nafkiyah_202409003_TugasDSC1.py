#!/usr/bin/env python
# coding: utf-8

# In[24]:


var1=[1,2,3,4]
print("1. Tipe dari var1 adalah",type(var1))
print("2. Panjang dari var1 adalah",len(var1))


# In[23]:


first=[11.25,18.0,20.0]
second=[10.75,9.50]
full=first+second
print("1. List first dan second digabungkan menjadi ->",full)
full.sort()
full.reverse()
full_sorted=full
print("2. Variabel full diurutkan secara descending menjadi:",full_sorted)


# In[22]:


area=[11.25,18.0,20.0,10.75,9.50]
print("1. Indeks dari 20.0 adalah",area.index(20.0))
print("2. 14.5 muncul di variabel area sebanyak",area.count(14.5),"kali")
area.append(24.5)
area.append(15.45)
print("3. Variabel area ditambah anggota 24.5 dan 15.45 menjadi ->",area)
area.reverse()
print("4. Urutan variabel area dibalik menjadi ->",area)


# In[31]:


import math
r=0.43
keliling=2*math.pi*r
print("1. Keliling lingkaran =",keliling)
luas=math.pi*r*r
print("2. Luas lingkaran =",luas)
print("3. Keliling:",keliling,"dan Luas:",luas)


# In[34]:


area_3=["hallway",11.25,"kitchen",18.0,"chill zone",20.0,"bedroom",10.75,"bathroom",10.50,"poolhouse",24.5,"garage",15.45]
del area_3[10:14]
print("1. Setelah nilai pada index 4 terakhir dihapus:",area_3)


# In[45]:


area_4=["hallway",11.25,"kitchen",18.0,"living room",20.0,"bedroom",10.75,"bathroom",9.50]
area_4.remove("bathroom")
area_4.insert(8,10.8)
print("1. Setelah nilai 'bathroom' diganti menjadi 10.8:",area_4)
area_4.remove("living room")
area_4.insert(4,"ruang tamu")
print("2. Setelah nilai 'living room' diganti menjadi 'ruang tamu':",area_4)

