<!--
* @Component: LanguageSwitcher.vue
* @Maintainer: J.K. Yang
* @Description: 语言切换组件
-->
<script setup lang="ts">
import config from "@/configs";
import { Icon } from "@iconify/vue";
import { useLocale } from "vuetify";
import { useCustomizeThemeStore } from "@/stores/customizeTheme";
const { current } = useLocale();
const { availableLocales } = config.locales;
const customizeTheme = useCustomizeThemeStore();

onMounted(() => {
  setLocale(customizeTheme.localCode);
});

const setLocale = (locale: string) => {
  current.value = locale;
  customizeTheme.setLocalCode(locale);
};
</script>
<template>
  <v-menu>
    <template v-slot:activator="{ props }">
      <v-btn 
      icon v-bind="props"
      v-for="locale in availableLocales"
      :key="locale.code"
      @click="setLocale(locale.code)"
      :active="locale.code === current"
      >
        <v-icon v-if="locale.label === 'Blind'" color="primary">mdi-human-white-cane</v-icon>
        <v-icon v-else-if="locale.label === 'Yr-5'" color="primary">mdi-teddy-bear</v-icon>
        <Icon v-else :icon="`twemoji:flag-${locale.name}`" class="mr-2" />
      </v-btn>
    </template>
    <!-- <v-list nav>
      <v-list-item
        v-for="locale in availableLocales"
        :key="locale.code"
        @click="setLocale(locale.code)"
        density="compact"
        :active="locale.code === current"
      >
        <template v-slot:prepend>
          <Icon :icon="`twemoji:flag-${locale.name}`" class="mr-2" />
        </template>
        <v-list-item-title> {{ locale.label }}</v-list-item-title>
      </v-list-item>
    </v-list> -->
  </v-menu>
</template>
