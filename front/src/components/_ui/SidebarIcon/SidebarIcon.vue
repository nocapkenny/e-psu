<script setup>
import { computed } from "vue";
import ExitIcon from "../../../assets/images/svg/Exit_Icon.svg";
import UserIcon from "../../../assets/images/svg/User_Icon.svg";
import CoursesIcon from "../../../assets/images/svg/Courses_Icon.svg";
import TableIcon from "../../../assets/images/svg/Table_Icon.svg";
import EditCourse from "../../../assets/images/svg/EditCourse_Icon.svg";
const props = defineProps({
  type: {
    type: String,
    default: "profile",
  },
  text: {
    type: String,
    default: "Профиль",
  },
});

const iconComponent = computed(() => {
  const icon = {
    profile: UserIcon,
    courses: CoursesIcon,
    table: TableIcon,
    editCourse: EditCourse,
  };
  return icon[props.type];
});
</script>

<template>
  <div class="sidebar-icon">
    <component
      :is="iconComponent"
      class="sidebar-icon__icon"
      v-if="iconComponent"
    />
    <p class="sidebar-icon__text">{{ props.text }}</p>
    <ExitIcon class="sidebar-icon__icon" v-if="props.type === 'exit'" />
  </div>
</template>

<style lang="scss" scoped src="./SiderbarIcon.scss" />
