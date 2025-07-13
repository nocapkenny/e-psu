<script setup>
import SidebarIcon from "../_ui/SidebarIcon/SidebarIcon.vue";
</script>

<template>
  <div class="sidebar">
    <h1 class="sidebar__title">E-PSU</h1>
    <div class="sidebar__icons">
      <SidebarIcon type="profile" text="Профиль" />
      <SidebarIcon type="table" text="Мои оценки" />
      <SidebarIcon type="courses" text="Мои курсы" />
      <SidebarIcon type="exit" text="Выйти" />
    </div>
  </div>
</template>

<style src="./Sidebar.scss" lang="scss" scoped />
