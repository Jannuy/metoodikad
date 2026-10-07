<script setup>
import { onMounted, ref } from "vue";

const summary = ref([]);
const loading = ref(true);
const error = ref("");

async function loadSummary() {
  try {
    const response = await fetch("/api/summary/");
    if (!response.ok) throw new Error("Ülevaate laadimine ebaõnnestus.");
    summary.value = await response.json();
  } catch (reason) {
    error.value = reason.message;
  } finally {
    loading.value = false;
  }
}

onMounted(loadSummary);
</script>

<template>
  <section class="card">
    <h2>Õppeainete ülevaade</h2>
    <p class="muted">Tagasiside põhjal arvutatud koondvaade.</p>
    <p v-if="loading">Laadin ülevaadet...</p>
    <p v-else-if="error" class="error">{{ error }}</p>
    <div v-else class="table-wrap">
      <table>
        <thead><tr><th>Õppeaine</th><th>Vastuseid</th><th>Keskmine</th></tr></thead>
        <tbody><tr v-if="!summary.length"><td colspan="3">Tagasisidet veel ei ole.</td></tr><tr v-for="item in summary" :key="item.subject"><td>{{ item.subject }}</td><td>{{ item.count }}</td><td>{{ item.average }}</td></tr></tbody>
      </table>
    </div>
  </section>
</template>
