<script setup lang="ts">
import SalesCard from "@/components/dashboard/SalesCard.vue";
import SourcesCard from "@/components/dashboard/SourcesCard.vue";
import ActivityCard from "@/components/dashboard/ActivityCard.vue";
import TableCard from "@/components/dashboard/TableCard.vue";
import TicketsCard from "@/components/dashboard/TicketsCard.vue";
// import TrackCard from "@/components/dashboard/TrackCard.vue";
import TodoCard from "@/components/dashboard/TodoCard.vue";
import TaskCard from "@/components/dashboard/ChartCard.vue";
</script>
<template>
  <div class="pa-5">
    <!-- ---------------------------------------------- -->
    <!---first Row -->
    <!-- ---------------------------------------------- -->
    <v-row class="card-shadow flex-grow-0" dense>
      <v-col cols="12" xl="6">
        <!-- Table Card-->
        <v-card class="card-shadow" height="420">
          <table-card></table-card>
        </v-card>
      </v-col>
      <v-col cols="12" xl="6">
        <!-- Traffic Card-->
        <v-card class="card-shadow h-full" height="420">
          <sources-card></sources-card>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>
<style lang="scss" scoped></style>
