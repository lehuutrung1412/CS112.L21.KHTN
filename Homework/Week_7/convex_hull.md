# Problem: Convex Hull using Geometric

## Abstraction

Tìm bao lồi tạo bởi n điểm và kiểm tra tập đỉnh đã cho có thuộc tập bao lồi không.

## Solution 1:

### Algorithm:

* Tìm bao lồi: Sử dụng giải thuật [Monotone chain](https://vnoi.info/wiki/translate/wcipeg/Convex-Hull#thu%E1%BA%ADt-to%C3%A1n-chu%E1%BB%97i-%C4%91%C6%A1n-%C4%91i%E1%BB%87u) (hoặc [Graham](https://vnoi.info/wiki/translate/wcipeg/Convex-Hull#thu%E1%BA%ADt-to%C3%A1n-graham)) (độ phức tạp O(nlogn))
    * Sắp xếp các điểm theo thứ tự tăng dần hoành độ, nếu cùng hoành độ thì tung độ nhỏ hơn đứng trước 
    * Xét lần lượt các điểm, nếu các điểm di chuyển ngược chiều kim đồng hồ thì thêm vào chuỗi dưới, còn cùng chiều kim đồng hồ thì thêm vào chuỗi trên
    * Gộp 2 chuỗi trên và dưới để lấy bao lồi
* So sánh 2 tập hợp: Dùng cấu trúc set với toán tử == (độ phức tạp O(k))

### Time Complexity:

Do k <= n nên độ phức tạp giải thuật này là O(nlogn)

## Solution 2:

### Algorithm:

- Duyệt qua từng vector cạnh theo thứ tự đa giác đã cho. Sau đó lần lượt tính tích có hướng của vector cạnh với vector tạo bởi gốc của vector cạnh đang xét với tất cả các đỉnh còn lại ngoài 2 đỉnh thuộc vector cạnh đang xét.
    - Nếu tất cả kết quả không âm thì duyệt qua cạnh khác
    - Nếu có kết quả âm thì break và báo "No"
- Sau khi duyệt hết tất cả các vector thì kết luận đa giác đã cho là bao lồi của tập n đỉnh

### Time Complexity:

- O(kn)
