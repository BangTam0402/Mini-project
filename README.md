##### \# 🎬 Hệ thống đặt vé xem phim (Movie Ticket Booking System)

##### &#x20;📌 Mô tả

##### Đây là chương trình quản lý đặt vé xem phim được xây dựng bằng ngôn ngữ Python, chạy trên giao diện dòng lệnh (CLI).

##### 

##### Chương trình cho phép người dùng thực hiện các thao tác như thêm vé, hiển thị danh sách, tìm kiếm, sắp xếp, thống kê và lưu trữ dữ liệu.

##### 

##### \---

##### 

##### \## Chức năng

##### 1\. Thêm vé (Add Ticket)

##### 

##### Chức năng này cho phép người dùng nhập thông tin của một vé xem phim bao gồm:

##### 

##### Mã vé (ID)

##### Tên phim

##### Tên khách hàng

##### Số ghế

##### Giá vé

##### 

##### Khi nhập, chương trình sẽ:

##### 

##### Kiểm tra xem ID đã tồn tại chưa để tránh trùng lặp

##### Kiểm tra giá vé có hợp lệ (phải là số và > 0)

##### Nếu dữ liệu hợp lệ, vé sẽ được thêm vào danh sách.

##### Nếu không hợp lệ, chương trình sẽ báo lỗi và không thêm dữ liệu

##### 2\. Hiển thị danh sách vé (Display Tickets)

##### 

##### Chức năng này dùng để hiển thị toàn bộ danh sách vé hiện có.

##### 

##### Dữ liệu được in ra dưới dạng bảng với các cột:

##### 

##### ID

##### Tên phim

##### Tên khách hàng

##### Số ghế

##### Giá vé

##### 

##### Giúp người dùng dễ quan sát và kiểm tra dữ liệu đã nhập.

##### 3\. Tìm kiếm vé (Search Ticket)

##### Chức năng này cho phép tìm kiếm vé dựa trên:

##### 

##### ID

##### hoặc

##### Tên khách hàng

##### 

##### Chương trình sẽ duyệt qua danh sách vé:

##### 

##### Nếu tìm thấy, hiển thị thông tin vé tương ứng

##### Nếu không tìm thấy, thông báo không có kết quả

##### 

##### 4\. Sắp xếp vé (Sort Tickets)

##### 

##### Chức năng này giúp sắp xếp danh sách vé theo một tiêu chí nhất định, ví dụ:

##### 

##### Theo giá vé

##### Theo tên phim

##### Theo tên khách hàng

##### 

##### Sau khi sắp xếp, danh sách sẽ được cập nhật lại giúp người dùng dễ theo dõi.

##### &#x20;6. Lưu dữ liệu vào file TXT (Save to TXT)

##### 

##### Chức năng này dùng để lưu toàn bộ danh sách vé vào file tickets.txt.

##### 

##### Mỗi vé được lưu trên một dòng với định dạng:

##### 

##### ID|Movie|Customer|Seat|Price

##### 

##### Việc lưu file giúp dữ liệu không bị mất khi tắt chương trình.

##### 

##### &#x20;7. Đọc dữ liệu từ file TXT (Load from TXT)

##### 

##### Chức năng này giúp đọc dữ liệu từ file tickets.txt khi khởi động chương trình.

##### 

##### Chương trình sẽ:

##### 

##### Đọc từng dòng trong file

##### Tách dữ liệu

##### Chuyển thành danh sách vé trong chương trình

##### 

##### Giúp khôi phục dữ liệu đã lưu trước đó.

##### 

##### &#x20;8. Tìm kiếm nâng cao (Advanced Search)

##### 

##### Chức năng này cho phép tìm kiếm linh hoạt hơn.

##### 

##### Người dùng có thể nhập một phần tên phim

##### Ví dụ:

##### 

##### Nhập: man

##### Kết quả: tìm được Spider Man

##### 

##### Chức năng này sử dụng tìm kiếm theo chuỗi con (substring).

##### 

##### &#x20;9. Thống kê nâng cao (Advanced Statistics)

##### 

##### Chức năng này thực hiện thống kê theo từng phim.

##### 

##### Chương trình sẽ:

##### 

##### Đếm số vé của mỗi phim

##### Hiển thị kết quả dạng:

##### Avengers : 2 vé

##### Spider Man : 3 vé

##### 

##### Giúp biết phim nào được đặt nhiều hơn.

##### 

##### &#x20;10. Xuất dữ liệu JSON (Export to JSON)

##### 

##### Chức năng này chuyển dữ liệu vé sang file tickets.json.

##### 

##### Dữ liệu được lưu dưới dạng JSON giúp:

##### 

##### Dễ đọc

##### Dễ sử dụng cho các hệ thống khác

##### &#x20;11. Nhập dữ liệu JSON (Import from JSON)

##### 

##### Chức năng này đọc dữ liệu từ file tickets.json và đưa vào chương trình.

##### 

##### Nếu file tồn tại:

##### 

##### Dữ liệu sẽ được nạp lại

##### 

##### Nếu không:

##### 

##### Chương trình sẽ thông báo lỗi

##### &#x20;12. Thoát chương trình (Exit)

##### 

##### Khi người dùng chọn thoát:

##### 

##### Dữ liệu sẽ được tự động lưu vào file TXT

##### Chương trình kết thúc

##### 

##### 

##### \## Công nghệ sử dụng

##### \- Python 3

##### \- Thư viện `json`

##### \- Xử lý file `.txt`

##### 

##### \---

##### 

##### \## Cách chạy chương trình

##### 

##### 1\. Cài đặt Python

##### 2\. Mở terminal hoặc command prompt

##### 3\. Chạy lệnh:

##### 

##### ```bash

##### python main.py

