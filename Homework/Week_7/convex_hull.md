# Problem: Convex Hull using Geometric

## Abstraction

Tìm bao lồi tạo bởi n điểm và kiểm tra tập đỉnh đã cho có thuộc tập bao lồi không.

## Algorithm:

* Tìm bao lồi: Sử dụng giải thuật Monotone chain (hoặc Graham) (độ phức tạp O(nlogn))
    * Sắp xếp các điểm theo thứ tự tăng dần hoành độ, nếu cùng hoành độ thì tung độ nhỏ hơn đứng trước 
    * Xét lần lượt các điểm, nếu các điểm di chuyển ngược chiều kim đồng hồ thì thêm vào chuỗi dưới, còn cùng chiều kim đồng hồ thì thêm vào chuỗi trên
    * Gộp 2 chuỗi trên và dưới để lấy bao lồi
* So sánh 2 tập hợp: Dùng cấu trúc set với toán tử == (độ phức tạp O(k))

## Time Complexity:

Do k <= n nên độ phức tạp giải thuật này là O(nlogn)