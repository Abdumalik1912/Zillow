from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm, CustomerUserForm, CustomerUserUpdateForm, ProfileForm, ProfileUpdateForm


class Login(View):
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Tizimga muvaffaqqiyatli kirdingiz")

                # foydalanuvchi login qilib audintifikatsiyadan o'tganda kerakli joyga jo'natish
                return redirect('home')
            else:
                # login qilolmasa  kerakli joyga jo'natish
                messages.error(request, 'Bunday login yoki parol mavjud emas')
                return render(request, 'footer.html', {'form': form})
        else:
            # validatsiyadan o'tmasa  kerakli joyga jo'natish
            messages.error(request, 'Login yoki parolda xatolik mavjud')
            return render(request, 'home', {'form': form})


class Logout(View):
    def post(self, request):
        messages.success(request, 'Tizimdan chiqdingiz')
        return render(request, 'index.html')


class Register(View):
    def post(self, request):
        form = CustomerUserForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                # Register qilaolganda kerakli joyga jo'natish
                messages.success(request, "Muvaffaqqiyatli ro'yxatdan o'tdingiz")
                return redirect('home')
        except:
            pass
        # Register qilolmasa  kerakli joyga jo'natish
        messages.error(request, "Ro'yxatdan o'tishda xatolik yuzaga keldi. Iltimos, qayta urinib ko'ring.")
        return render(request, 'register.html', {'form': form})


class CustomUserUpdate(View):
    def get(self, request):
        form = CustomerUserUpdateForm(instance=request.user)
        return render(request, 'update_user_form.html', {'form': form})

    def post(self, request):
        form = CustomerUserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Muvaffaqqiyatli ma'lumotlarni yangiladingiz")
            # Ma'lumotlari o'zgarganda kerakli joyga jo'natish
            return redirect('home')
        else:
            messages.error(request, "Ma'lumotlarni yangilashda xatolik yuzaga keldi. Qayta urinib ko'ring.")
        return render(request, 'update_user_form.html', {'form': form})


class Profile(View):
    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile muvaffaqqiyatli yaratildi')
            # Profile yaratilganda kerakli joyga jo'natish
            return redirect('home')
        else:
            messages.error(request, "Profile yaratishda xatolik yuzaga keldi. Qayta urinib ko'ring.")
        return render(request, 'home', {'form': form})


class ProfileUpdate(View):
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, 'update_profile_form.html', {'form': form})

    def post(self, request):
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Muvaffaqqiyatli ma'lumotlarni yangiladingiz")
            # Ma'lumotlari o'zgarganda kerakli joyga jo'natish
            return redirect('home')
        else:
            messages.error(request, "Ma'lumotlarni yangilashda xatolik yuzaga keldi. Qayta urinib ko'ring.")
        return render(request, 'update_profile_form.html', {'form': form})