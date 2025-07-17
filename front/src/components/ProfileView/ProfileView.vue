<script setup></script>

<template>
  <section class="profile">
    <div class="container">
        <div class="profile__inner">
            <div class="profile__content">
                <div class="profile__content-box">
                    <img src="../../assets/images/Profile_Avatar.jpg" alt="avatarImg" class="profile__box-img" loading="lazy">
                </div>
                <div class="profile__content-info">
                    <h2 class="profile__info-title">Егор Безродный</h2>
                    <a class="profile__info-email profile__info-text" href="mailto:pochta@yandex.ru">Email: pochta@yandex.ru</a>
                    <p class="profile__info-type profile__info-text">Тип пользователя: Студент</p>
                    <p class="profile__info-group profile__info-text">Группа: ИТХ-12-23</p>
                </div>
            </div>
            <div class="profile__schedule">
                <h3 class="profile__schedule-title">Расписание</h3>
                <p class="profile__schedule-text">Здесь будет расписание</p>
            </div>
        </div>
    </div>
  </section>
</template>

<style lang="scss" scoped src="./ProfileView.scss" />
