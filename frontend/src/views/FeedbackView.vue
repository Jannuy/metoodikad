<script setup>
import { reactive, ref } from "vue";

const subjects = [
  "Matemaatika",
  "Vene keel",
  "Andmebaasid",
  "Programmeerimine",
  "Inglise keel",
  "Füüsika",
  "Keemia",
  "Kunst",
];

const form = reactive({ name: "", class_name: "", subject: "", rating: "", comment: "" });
const errors = ref({});
const success = ref("");
const saving = ref(false);

async function submitFeedback() {
  errors.value = {};
  success.value = "";
  saving.value = true;

  try {
    const response = await fetch("/api/feedback/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ...form, rating: Number(form.rating) }),
    });
    const payload = await response.json();
    if (!response.ok) {
      errors.value = payload;
      return;
    }
    Object.assign(form, { name: "", class_name: "", subject: "", rating: "", comment: "" });
    success.value = "Tagasiside on edukalt salvestatud!";
  } catch {
    errors.value = { non_field_errors: ["Serveriga ühenduse loomine ebaõnnestus."] };
  } finally {
    saving.value = false;
  }
}
</script>

<template>
  <section class="card">
    <h2>Tagasiside vorm</h2>
    <form @submit.prevent="submitFeedback">
      <div class="grid">
        <label>Nimi<input v-model="form.name" type="text" placeholder="Sisesta oma nimi" /><small>{{ errors.name?.[0] }}</small></label>
        <label>Klass<input v-model="form.class_name" type="text" placeholder="Näiteks 10.B" /><small>{{ errors.class_name?.[0] }}</small></label>
      </div>
      <label>Õppeaine<select v-model="form.subject" required><option value="">Vali õppeaine</option><option v-for="subject in subjects" :key="subject" :value="subject">{{ subject }}</option></select><small>{{ errors.subject?.[0] }}</small></label>
      <fieldset><legend>Hinne</legend><div class="rating"><label v-for="rating in 5" :key="rating"><input v-model="form.rating" type="radio" name="rating" :value="rating" /> {{ rating }}</label></div><small>{{ errors.rating?.[0] }}</small></fieldset>
      <label>Kommentaar <span>(valikuline)</span><textarea v-model="form.comment" maxlength="500" placeholder="Kirjuta soovi korral kommentaar..." /><small>{{ errors.comment?.[0] }}</small></label>
      <button type="submit" :disabled="saving">{{ saving ? "Salvestan..." : "Saada tagasiside" }}</button>
      <p v-if="success" class="success">{{ success }}</p>
      <p v-if="errors.non_field_errors" class="error">{{ errors.non_field_errors[0] }}</p>
    </form>
  </section>
</template>
