import enMessages from "@/locales/en";
import zhHansMessages from "@/locales/zhHans";
import paMessages from "@/locales/pa";
import jaMessages from "@/locales/ja";


const supported = ["en", "zhHans", "ja", "pa"];
let locale = "en";

try {
  const { 0: browserLang } = navigator.language.split("-");
  if (supported.includes(browserLang)) locale = browserLang;
} catch (e) {
  console.log(e);
}

export default {
  // current locale
  locale,

  // when translation is not available fallback to that locale
  fallbackLocale: "en",

  // availabled locales for user selection
  availableLocales: [
    {
      code: "blind",
      flag: "au",
      name: "australia",
      label: "Blind",
      messages: enMessages,
    },
    {
      code: "yr-5",
      flag: "au",
      name: "australia",
      label: "Yr-5",
      messages: enMessages,
    },
    {
      code: "en",
      flag: "au",
      name: "australia",
      label: "English",
      messages: enMessages,
    },
    {
      code: "zhHans",
      flag: "cn",
      name: "china",
      label: "中文",
      messages: zhHansMessages,
    },
    {
      code: "pa",
      flag: "pa",
      name: "india",
      label: "Pubjubi",
      messages: paMessages,
    },
    {
      code: "ja",
      flag: "jp",
      name: "japan",
      label: "日本語",
      messages: jaMessages,
    },
  ],
  messages: {
    en: enMessages,
    zhHans: zhHansMessages,
    pa: paMessages,
    ja: jaMessages,
  },
};
