# Homework week 1: Algorithm Analysis

## 1. Bài 1: W(n), A(n) lần lượt là thời gian chạy trường hợp xấu nhất và trung bình của thuật toán có kích thước là n. Điều nào dưới đây luôn đúng?

<img src="Bai1.png" alt="Bài 1" width="300"/>

- [x] Chọn đáp án C

## 2. Bài 2: Độ phức tạp của hàm fun()?

<img src="Bai2.png" alt="Bài 2" width="400">

* Ở vòng for thứ nhất, với i = n thì vòng for thứ 2 sẽ chạy n lần
* Ở vòng for thứ nhất, với i = n/2 thì vòng for thứ 2 sẽ chạy n/2 lần
* Ở vòng for thứ nhất, với i = n/4 thì vòng for thứ 2 sẽ chạy n/4 lần
* ...
* Ở vòng for thứ nhất, với i = 1 thì vòng for thứ 2 sẽ chạy 1 lần

Như vậy số lần chạy cho cả 2 vòng for là: n + n/2 + n/4 + ... + 1

=> Độ phức tạp hàm fun(): O(n + n/2 + n/4 + ... + 1) = O(n)

## 3. Bài 3: Độ phức tạp của hàm đệ quy sau là bao nhiêu?

<img src="Bai3.png" alt="Bài 3" width="400">

## 4. Bài 4: Độ phức tạp xấu nhất khi thực hiện đoạn chương trình?

<img src="Bai4.png" alt="Bài 4" width="400">