### 要求三
1. 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
   ```mysql
   insert into member(name,username,password)
   values('test','test','test');
   insert into member(name,username,password)
   values('Amy Wang','Amy','iamamy');
   insert into member(name,username,password)
   values('Claire Su','Claire','iamclaire');
   insert into member(name,username,password)
   values('Max Lin','Max','iammax');
   insert into member(name,username,password)
   values('Alen Chau','Alen','iamalen');
   insert into member(name,username,password)
   values('Ivy Chuang','Ivy','iamivy');
   insert into member(name,username,password)
   values('Ian Chu','Ian','iamian');
   ```
   ![3-1](https://user-images.githubusercontent.com/111445341/196464900-8de91c07-dd37-4f0f-bdb1-6daa3f972c0a.png)

2. 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。
   ```mysql
   select * from member;
   ```
   ![3-2 ](https://user-images.githubusercontent.com/111445341/196473140-a0ef7ba9-1cf1-43ed-9916-f16f78199c53.png)

3. 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
   ```mysql
   select * from member order by time desc;
   ```
   ![3-3](https://user-images.githubusercontent.com/111445341/196473647-53baf3e3-fbc6-499e-9c46-da7a1d5e0f5b.png)
   
4. 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )
   ```mysql
   select * from member order by time desc limit 1,3;
   ```
   ![3-4](https://user-images.githubusercontent.com/111445341/196474002-9bec69da-47f0-45f1-9f17-77708fc4acf8.png)
   
5. 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。
   ```mysql
   select * from member where username = 'test';
   ```
   ![3-5](https://user-images.githubusercontent.com/111445341/196474389-938d9a26-2338-4c20-8784-977e56a01e42.png)
   
6. 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
   ```mysql
   select * from member where username = 'test' and password = 'test';
   ```
   ![3 6](https://user-images.githubusercontent.com/111445341/196474653-72fd18aa-036a-49f2-9bcd-9ee640c29f5e.png)
   
7. 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
   ```mysql
   update member set name = 'test2' where username = 'test';
   ```
   ![3-7](https://user-images.githubusercontent.com/111445341/196475054-122d70bd-d8fb-43fe-b96c-bd14a668feb3.png)

### 要求四
1. 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
   ```mysql
   select count(id) from member;
   ```
   ![4-1](https://user-images.githubusercontent.com/111445341/196475510-9cb95384-85cf-4f8a-b647-bc63ea1380df.png)
   
2. 取得 member 資料表中，所有會員 follower_count 欄位的總和。
   ```mysql
   select sum(follower_count) from member;
   ```
   ![4-2](https://user-images.githubusercontent.com/111445341/196475799-29b265ea-9dc6-47ae-bda7-3b8178ca8aae.png)

3. 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
   ```mysql
   select avg(follower_count) from member;
   ```
   ![4 3](https://user-images.githubusercontent.com/111445341/196476065-698ad022-99ac-4df5-8141-05ca5e891f07.png)

### 要求五
在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message 。資料表中必須包含以下欄位設定：
```mysql
create table message(
id bigint primary key auto_incrment,
member_id bigint not null,
foreign key(member_id) references member(id),
content varchar(255) not null,
like_count int unsigned not null default 0,
time datetime not null default current_timestamp);
```
![5](https://user-images.githubusercontent.com/111445341/196476854-9309b914-2cd0-409d-85ec-8100d097be4f.png)

1. 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
   ```mysql
   select message.content,member.username
   from message 
   inner join member on message.member_id = member.id;
   ```
   ![5-1](https://user-images.githubusercontent.com/111445341/196477464-6dccf778-6479-42d8-bea6-4aaa96ea0bdf.png)
 
2. 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
   ```mysql
   select member.username,message.content
   from member 
   inner join message on message.member_id = member.id
   where member.username = 'test';
   ```
   ![5-2](https://user-images.githubusercontent.com/111445341/196477930-019345f1-160f-4c2b-9238-c8108826cedd.png)
   
3. 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
   ```mysql
   select avg(message.like_count) 
   from member 
   inner join message on message.member_id = member.id
   where member.username = 'test';
   ```
   ![5-3](https://user-images.githubusercontent.com/111445341/196478461-454217f6-a80b-4359-a2a8-6bf0fa66bbf6.png)

   
   
   


   
   
   

   
   
