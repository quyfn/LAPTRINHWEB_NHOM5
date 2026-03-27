from django.shortcuts import render


SPA_IMAGES = {
    "collagen": "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=1200&q=80",
    "anti-acne": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?auto=format&fit=crop&w=1200&q=80",
    "massage": "https://images.unsplash.com/photo-1519823551278-64ac92734fb1?auto=format&fit=crop&w=1200&q=80",
    "laser": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=1200&q=80",
    "head-spa": "https://images.unsplash.com/photo-1519415510236-718bdfcd89c8?auto=format&fit=crop&w=1200&q=80",
    "detox": "https://images.unsplash.com/photo-1507652313519-d4e9174996dd?auto=format&fit=crop&w=1200&q=80",
    "hero-massage": "https://images.unsplash.com/photo-1515377905703-c4788e51af15?auto=format&fit=crop&w=900&q=80",
    "hero-sauna": "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?auto=format&fit=crop&w=900&q=80",
    "hero-neck": "https://images.unsplash.com/photo-1519824145371-296894a0daa9?auto=format&fit=crop&w=900&q=80",
    "review-1": "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=800&q=80",
    "review-2": "https://images.unsplash.com/photo-1512290923902-8a9f81dc236c?auto=format&fit=crop&w=800&q=80",
    "review-3": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=800&q=80",
    "review-4": "https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=800&q=80",
    "review-5": "https://images.unsplash.com/photo-1526045612212-70caf35c14df?auto=format&fit=crop&w=800&q=80",
    "review-6": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80",
    "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80",
}


NAV_ITEMS = [
    {"label": "Dịch vụ", "url": "/services/", "key": "services"},
    {"label": "Tư vấn", "url": "/consult/", "key": "consult"},
    {"label": "Đánh giá", "url": "/reviews/", "key": "reviews"},
    {"label": "Tài khoản", "url": "/account/profile/", "key": "account"},
]


SERVICE_CATEGORIES = ["Tất cả", "Da mặt", "Body", "Triệt lông", "Giá"]


SERVICE_LIST = [
    {
        "slug": "collagen",
        "title": "Chăm sóc da mặt Collagen",
        "subtitle": "Làm sạch sâu, dưỡng ẩm và tái tạo da",
        "time": "90 phút",
        "price": "1,200,000đ",
        "rating": "4.8",
        "theme": "theme-blush",
    },
    {
        "slug": "anti-acne",
        "title": "Trị mụn chuyên sâu",
        "subtitle": "Điều trị mụn an toàn, hiệu quả",
        "time": "60 phút",
        "price": "500,000đ",
        "rating": "4.5",
        "theme": "theme-ivory",
    },
    {
        "slug": "massage",
        "title": "Massage body thư giãn",
        "subtitle": "Massage toàn thân giúp thư giãn",
        "time": "60 phút",
        "price": "500,000đ",
        "rating": "4.6",
        "theme": "theme-rose",
    },
    {
        "slug": "laser",
        "title": "Triệt lông vĩnh viễn bằng laser/IPL",
        "subtitle": "Triệt lông vĩnh viễn bằng laser/IPL",
        "time": "90 phút",
        "price": "2,000,000đ",
        "rating": "4.8",
        "theme": "theme-pearl",
    },
    {
        "slug": "head-spa",
        "title": "Trị rụng tóc / gàu",
        "subtitle": "Giúp làm sạch sâu, giảm bã nhờn",
        "time": "60 phút",
        "price": "1,300,000đ",
        "rating": "4.7",
        "theme": "theme-sand",
    },
    {
        "slug": "detox",
        "title": "Xông hơi sauna",
        "subtitle": "Giãn nở lỗ chân lông, đào thải độc tố",
        "time": "90 phút",
        "price": "700,000đ",
        "rating": "4.9",
        "theme": "theme-apricot",
    },
]


FOOTER_SERVICES = ["Chăm sóc da mặt", "Massage body", "Triệt lông", "Điều trị mụn", "Tắm trắng"]


FOOTER_ABOUT = ["Giới thiệu", "Đội ngũ", "Tin tức", "Liên hệ", "Tuyển dụng"]


CONTACT = {
    "address": "104/7 Lê Đình Lý, Thanh Khê, Đà Nẵng",
    "phone": "0901 234 589",
    "email": "info@maitram.spa",
}


def review_items_data():
    return [
        {"id": 1, "title": "Thanh lọc da", "status": "Đã đánh giá", "status_class": "status-green", "theme": "theme-ivory", "image": SPA_IMAGES["review-1"], "date": "28/02/2026", "staff": "Nguyễn Ngọc Anh"},
        {"id": 2, "title": "Massage cổ vai gáy", "status": "Đã đánh giá", "status_class": "status-green", "theme": "theme-pearl", "image": SPA_IMAGES["review-2"], "date": "18/02/2026", "staff": "Lê Minh Châu"},
        {"id": 3, "title": "Dưỡng da chuyên sâu", "status": "Chưa đánh giá", "status_class": "status-red", "theme": "theme-blush", "image": SPA_IMAGES["review-3"], "date": "01/01/2026", "staff": "Trần Thị Mai"},
        {"id": 4, "title": "Massage body đá nóng", "status": "Chưa đánh giá", "status_class": "status-red", "theme": "theme-cocoa", "image": SPA_IMAGES["review-4"], "date": "26/12/2025", "staff": "Hồng Nhung"},
        {"id": 5, "title": "Chăm sóc gương mặt", "status": "Đã đánh giá", "status_class": "status-green", "theme": "theme-apricot", "image": SPA_IMAGES["review-5"], "date": "20/12/2025", "staff": "Nguyễn Thu Hương"},
        {"id": 6, "title": "Gội đầu dưỡng sinh", "status": "Chưa đánh giá", "status_class": "status-red", "theme": "theme-cocoa", "image": SPA_IMAGES["review-6"], "date": "15/12/2025", "staff": "Phạm Ngọc Hân"},
    ]


def base_context(active_path: str) -> dict:
    if active_path.startswith("/services"):
        current_section = "services"
    elif active_path.startswith("/consult"):
        current_section = "consult"
    elif active_path.startswith("/reviews"):
        current_section = "reviews"
    elif active_path.startswith("/account"):
        current_section = "account"
    else:
        current_section = ""

    return {
        "nav_items": NAV_ITEMS,
        "active_path": active_path,
        "current_section": current_section,
        "footer_services": FOOTER_SERVICES,
        "footer_about": FOOTER_ABOUT,
        "contact": CONTACT,
        "booking_cta_url": "/account/?next=/booking/service/",
    }


def home(request):
    context = base_context(request.path)
    context["hero_cards"] = [
        {"title": "Massage thư giãn", "shape": "arch", "theme": "theme-warm", "image": SPA_IMAGES["hero-massage"]},
        {"title": "Sauna trị liệu", "shape": "circle", "theme": "theme-gold", "image": SPA_IMAGES["hero-sauna"]},
        {"title": "Chăm sóc cổ vai gáy", "shape": "tall", "theme": "theme-cocoa", "image": SPA_IMAGES["hero-neck"]},
    ]
    return render(request, "spa/home.html", context)


def services(request):
    context = base_context(request.path)
    context["categories"] = SERVICE_CATEGORIES
    context["services"] = [{**item, "image": SPA_IMAGES[item["slug"]]} for item in SERVICE_LIST]
    return render(request, "spa/services.html", context)


def service_detail(request):
    context = base_context("/services/")
    context["service"] = {**SERVICE_LIST[0], "image": SPA_IMAGES[SERVICE_LIST[0]["slug"]]}
    context["gallery"] = [
        {"theme": "theme-blush", "image": SPA_IMAGES["collagen"]},
        {"theme": "theme-cocoa", "image": SPA_IMAGES["massage"]},
        {"theme": "theme-apricot", "image": SPA_IMAGES["detox"]},
        {"theme": "theme-lilac", "image": SPA_IMAGES["laser"]},
    ]
    context["benefits"] = [
        "Da sáng mịn, đều màu và có độ đàn hồi tốt hơn",
        "Giảm mụn, sạch dầu và thu nhỏ lỗ chân lông",
        "Trẻ hóa da, giảm nếp nhăn nhẹ một cách tự nhiên",
        "An toàn cho da nhạy cảm, được kiểm chứng lâm sàng",
    ]
    context["steps"] = [
        "Chuyên viên phân tích da, xác định loại da và lựa chọn dưỡng chất phù hợp.",
        "Làm sạch sâu bằng công nghệ gentle cleansing, loại bỏ tạp chất từ đầu lông tơ.",
        "Đắp mặt nạ dưỡng chất, sử dụng serum cao cấp để nuôi dưỡng tái tạo da.",
        "Massage mặt bằng đá cuội và dưỡng ẩm locking, kết thúc bằng kem chống nắng.",
    ]
    return render(request, "spa/service_detail.html", context)


def account(request):
    context = base_context(request.path)
    context["next_url"] = request.GET.get("next", "/booking/service/")
    return render(request, "spa/account.html", context)


def account_base_context(active_path: str) -> dict:
    context = base_context(active_path)
    context["account_links"] = [
        {"label": "Thông tin cá nhân", "url": "/account/profile/", "key": "profile"},
        {"label": "Lịch sử dịch vụ", "url": "/account/history/", "key": "history"},
        {"label": "Điểm tích lũy", "url": "/account/points/", "key": "points"},
    ]
    return context


def account_profile(request):
    context = account_base_context(request.path)
    form_data = {
        "name": "Lê Thị Quỳnh Như",
        "phone": "0996834824",
        "email": "lenhuli674@gmail.com",
        "birthday": "07 / 07 / 2005",
        "address": "Hải Châu, Đà Nẵng",
        "note": "Thông tin sức khỏe, sở thích điều trị, ...",
    }
    context["account_active"] = "profile"
    context["show_success"] = False
    context["show_error"] = False
    context["profile_avatar"] = SPA_IMAGES["avatar"]
    if request.method == "POST":
        form_data = {
            "name": request.POST.get("name", ""),
            "phone": request.POST.get("phone", ""),
            "email": request.POST.get("email", ""),
            "birthday": request.POST.get("birthday", ""),
            "address": request.POST.get("address", ""),
            "note": request.POST.get("note", ""),
        }
        digits = "".join(ch for ch in form_data["phone"] if ch.isdigit())
        if len(digits) != 10:
            context["show_error"] = True
        else:
            context["show_success"] = True
    context["form_data"] = form_data
    return render(request, "spa/account_profile.html", context)


def account_history(request):
    context = account_base_context(request.path)
    context["account_active"] = "history"
    context["history_rows"] = [
        ("28/01/2026", "Chăm sóc da mặt cao cấp", "Ngọc Anh", "1,500,000đ", "Hoàn thành"),
        ("10/01/2026", "Massage body thư giãn", "Minh Châu", "1,200,000đ", "Hoàn thành"),
        ("28/12/2026", "Triệt lông vĩnh viễn", "Thu Hương", "1,800,000đ", "Hoàn thành"),
        ("15/12/2026", "Chăm sóc da mặt cơ bản", "Ngọc Anh", "800,000đ", "Hoàn thành"),
        ("01/12/2026", "Gội đầu dưỡng sinh", "Hồng Nhung", "500,000đ", "Hoàn thành"),
    ]
    return render(request, "spa/account_history.html", context)


def account_points(request):
    context = account_base_context(request.path)
    context["account_active"] = "points"
    context["point_total"] = "1,250"
    context["point_rows"] = [
        ("28/01/2026", "Chăm sóc da mặt cao cấp", "+150", "1,250"),
        ("15/01/2026", "Đổi điểm lấy voucher", "-200", "1,100"),
        ("10/01/2026", "Massage body thư giãn", "+120", "1,300"),
        ("28/12/2026", "Triệt lông vĩnh viễn", "+180", "1,180"),
        ("15/12/2026", "Chăm sóc da mặt cơ bản", "+100", "1,000"),
    ]
    return render(request, "spa/account_points.html", context)


def consult(request):
    context = base_context(request.path)
    context["questions"] = [
        {
            "question": "Da nhạy cảm có thể làm liệu trình massage hoặc chăm sóc mặt không?",
            "answer": "Chúng tôi có các liệu trình dành riêng cho da nhạy cảm, sử dụng sản phẩm dịu nhẹ, không gây kích ứng, và nhân viên sẽ tư vấn trước khi thực hiện.",
        },
        {
            "question": "Liệu trình làm trắng da có an toàn cho da nhạy cảm không?",
            "answer": "Spa sử dụng sản phẩm chuyên dụng cho da nhạy cảm và kỹ thuật viên được đào tạo để giảm nguy cơ kích ứng. Khách hàng sẽ được thử một vùng nhỏ trước khi tiến hành toàn bộ liệu trình.",
        },
        {
            "question": "Sau khi lăn kim hoặc peel da, tôi cần bao lâu để da phục hồi hoàn toàn?",
            "answer": "Thời gian phục hồi tùy vào cơ địa và độ sâu của liệu trình. Thông thường da sẽ hồi phục từ 3-7 ngày. Nhân viên sẽ hướng dẫn cách chăm sóc tại nhà để da hồi phục nhanh và hiệu quả.",
        },
    ]
    context["chat_open"] = request.GET.get("chat") == "open"
    context["messages"] = [
        {"from": "guest", "text": "Shop ơi tư vấn này giúp e với về gói chăm da với"},
        {"from": "spa", "text": "Chào mừng bạn đến với dịch vụ Mai Trâm, bạn vui lòng đợi một chút sẽ có nhân viên tư vấn cho bạn ạ!"},
        {"from": "guest", "text": "Shop ơi tư vấn ạ"},
        {"from": "spa", "text": "Em đây ạ"},
    ]
    return render(request, "spa/consult.html", context)


def reviews(request):
    context = base_context(request.path)
    context["review_filters"] = [
        {"label": "Tất cả", "url": "/reviews/", "active": request.GET.get("tab", "all") == "all"},
        {"label": "Chưa đánh giá", "url": "/reviews/?tab=pending", "active": request.GET.get("tab") == "pending"},
        {"label": "Đã đánh giá", "url": "/reviews/?tab=done", "active": request.GET.get("tab") == "done"},
    ]
    context["review_items"] = review_items_data()
    tab = request.GET.get("tab", "all")
    if tab == "pending":
        context["review_items"] = [item for item in context["review_items"] if item["status"] == "Chưa đánh giá"]
    elif tab == "done":
        context["review_items"] = [item for item in context["review_items"] if item["status"] == "Đã đánh giá"]
    context["empty_state"] = not context["review_items"]
    return render(request, "spa/reviews.html", context)


def review_service_detail(request):
    context = base_context("/reviews/")
    context["modal_variant"] = request.GET.get("state", "pending")
    context["review_items"] = review_items_data()
    context["selected_review"] = context["review_items"][2 if context["modal_variant"] != "done" else 0]
    return render(request, "spa/review_service_detail.html", context)


def review_write(request):
    context = base_context("/reviews/")
    review_item = review_items_data()[2]
    context["review_item"] = review_item
    context["success"] = request.method == "POST" or request.GET.get("success") == "1"
    context["review_form"] = {
        "title": request.POST.get("title", "Da mượt và thư giãn hơn sau buổi trị liệu"),
        "content": request.POST.get("content", "Nhân viên tư vấn kỹ, thao tác nhẹ nhàng và không gian sạch sẽ. Sau buổi làm da ẩm hơn rõ rệt, mình sẽ quay lại thêm."),
        "rating": request.POST.get("rating", "5"),
    }
    return render(request, "spa/review_write.html", context)


def review_detail(request):
    context = base_context("/reviews/")
    context["confirm_delete"] = request.GET.get("confirm") == "1"
    context["review_item"] = review_items_data()[0]
    return render(request, "spa/review_detail.html", context)


def review_delete_success(request):
    context = base_context("/reviews/")
    context["review_items"] = review_items_data()
    return render(request, "spa/review_delete_success.html", context)


def booking_base_context(active_step: int, request_path: str) -> dict:
    context = base_context(request_path)
    context["booking_steps"] = [
        {"number": 1, "label": "Chọn dịch vụ", "url": "/booking/service/"},
        {"number": 2, "label": "Chọn gói", "url": "/booking/package/"},
        {"number": 3, "label": "Chọn thời gian", "url": "/booking/time/"},
        {"number": 4, "label": "Xác nhận", "url": "/booking/confirm/"},
    ]
    context["active_step"] = active_step
    context["sidebar_active"] = "booking" if request_path != "/appointments/" else "appointments"
    return context


def booking_service(request):
    context = booking_base_context(1, request.path)
    context["services"] = SERVICE_LIST
    context["selected_slug"] = "anti-acne"
    return render(request, "spa/booking_service.html", context)


def booking_package(request):
    context = booking_base_context(2, request.path)
    context["packages"] = [
        {
            "name": "Gói cơ bản",
            "features": ["1-2 buổi điều trị", "Làm sạch da cơ bản", "Massage mặt thư giãn", "Đắp mặt nạ Collagen", "Dưỡng ẩm hoàn thiện"],
            "price": "800,000đ",
            "note": "Phù hợp cho lần đầu trải nghiệm",
            "theme": "",
        },
        {
            "name": "Gói tiêu chuẩn",
            "features": ["3-5 buổi điều trị", "Tất cả quyền lợi gói cơ bản", "Tẩy tế bào chết chuyên sâu", "Serum dưỡng da cao cấp", "Tư vấn chăm sóc da tại nhà", "Tặng 1 mặt nạ collagen về nhà"],
            "price": "1,300,000đ",
            "note": "Hiệu quả rõ rệt sau 1 tháng",
            "theme": "is-selected soft-pink",
        },
        {
            "name": "Gói cao cấp",
            "features": ["8-10 buổi điều trị", "Tất cả quyền lợi gói tiêu chuẩn", "Công nghệ điều trị tiên tiến", "Massage vai gáy miễn phí", "Tặng bộ skincare mini", "Ưu đãi 10% dịch vụ tiếp theo"],
            "price": "2,500,000đ",
            "note": "Chăm sóc toàn diện, hiệu quả tối ưu",
            "theme": "soft-blush",
        },
        {
            "name": "Gói VIP",
            "features": ["12-15 buổi điều trị", "Tất cả quyền lợi gói cao cấp", "Phòng riêng VIP sang trọng", "Thư giãn xông đá trước miễn phí", "Tặng bộ skincare cao cấp", "Ưu đãi 20% mọi dịch vụ"],
            "price": "3,500,000đ",
            "note": "Trải nghiệm đẳng cấp 5 sao",
            "theme": "soft-gold",
        },
    ]
    return render(request, "spa/booking_package.html", context)


def booking_time(request):
    context = booking_base_context(3, request.path)
    context["times"] = [
        "08:00", "09:00", "10:00",
        "11:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00",
    ]
    context["calendar_days"] = list(range(1, 29))
    context["selected_day"] = 25
    context["selected_time"] = "16:00"
    context["show_times"] = request.GET.get("full") == "1"
    return render(request, "spa/booking_time.html", context)


def booking_confirm(request):
    context = booking_base_context(4, request.path)
    context["booking_info"] = {
        "service": "Trị mụn chuyên sâu",
        "package": "Gói cơ bản",
        "date": "25/02/2026",
        "time": "16:00",
        "name": "Nguyễn Thị Trà My",
        "phone": "0395672834",
        "email": "myhihahiha@gmail.com",
    }
    return render(request, "spa/booking_confirm.html", context)


def appointments(request):
    context = booking_base_context(0, request.path)
    context["appointments"] = [
        {
            "type": "Tư vấn",
            "title": "Tư vấn chăm sóc da",
            "date": "Thứ Năm, 05/02/2026",
            "time": "09:00",
            "package": "",
            "status": "Đã hủy",
            "status_class": "status-red",
        },
        {
            "type": "Dịch vụ",
            "title": "Chăm sóc da mặt",
            "date": "Thứ Tư, 04/02/2026",
            "time": "10:00",
            "package": "Gói VIP",
            "status": "Đã xác nhận",
            "status_class": "status-green",
            "action": "Yêu cầu hủy",
            "action_class": "status-red",
        },
        {
            "type": "Dịch vụ",
            "title": "Trị nám, tàn nhang",
            "date": "Chủ Nhật, 02/02/2026",
            "time": "14:00",
            "package": "Gói cao cấp",
            "status": "Hoàn thành",
            "status_class": "status-blue",
        },
    ]
    return render(request, "spa/appointments.html", context)
