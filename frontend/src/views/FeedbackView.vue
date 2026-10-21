<script setup>
import { reactive, ref } from "vue";

const subjects = [
  "Digioskuste arendamine",
  "Õpitee",
  "IT valdkonna alusteadmised",
  "Eesti keel",
  "Minapilt",
  "Programmeerimise alused",
  "Matemaatika",
  "Liikumised ja jõud",
  "Loodusteaduste metodoloogia",
  "Inglise keel",
  "Suhtlemiseõpetus",
  "Elektroonika ja digitehnika alused",
  "Sidetehnoloogiate areng",
  "Elektrotehnika",
  "Materjaliõpetus",
  "Elektroonikakomponendid",
  "Keemia",
  "Töö- ja mõõteriistad, tööohutus",
  "Kujundus- ja fototöötlustarkvara",
  "Tasapinnaline ja ruumiline geomeetria",
  "Valdkonna põhialused",
  "Karjäär energeetika sektoris ja ohutus",
  "Linux operatsioonisüsteemid",
  "Ajalugu",
  "Energia",
  "Kehakultuur",
  "Keel ja kirjandus",
  "Rakendusserverid ja teenused",
  "Ühiskonnaõpetus",
  "Arvutivõrgud",
  "Veebirakenduste loomine",
  "Keemia alused ja anorgaanilised ained",
  "IT-süsteemide alused",
  "Infoturve",
  "IP-võrgud ja uued tehnoloogiad",
  "Video- ja animatsiooni alused",
  "Elekter ja magnetism",
  "Pikselgraafika",
  "Trükitehnikad ja trükkimine",
  "Orgaanilised ained",
  "Vektorgraafika",
  "Trükiste tootmise protsess",
  "Vene keel",
  "Pilveteenuste alused",
  "Automatiseerimine Linuxi platvormil",
  "Andmebaasi serverite haldus",
  "Pilveteenuste haldus",
  "Kliendiseadmete halduse alused",
  "Blockchange",
  "Serveripoolsed tehnoloogiad veebirakenduse loomiseks",
  "Hajusrakendused",
  "Küberturbe alused",
  "Andmebaasid",
  "Tarkvaraarenduse meetodid",
  "Mobiilirakenduste loomise alused",
  "Testimise alused ja testimisplaan",
  "Arvutimängude loomine",
  "Elektrikilbi koostetööd",
  "Digitaaltehnika",
  "Erialane inglise keel",
  "Käidu alused",
  "Elektroonika alused",
  "Eesti keel teise keelena",
  "Soojustehnika alused",
  "Pneumoautomaatika",
  "Rakenduselektroonika",
  "Majanduse ja ettevõtluse alused",
  "Kõrgepingetehnika",
  "Karjääritee",
  "Eriotstarbeline tarkvara",
  "Elektrialane seadusandlus",
  "Elektriajamid ja nende juhtimine",
  "Elektriseadmete ja -paigaldiste käit",
  "Tööstuslikud elektriseadmed ja -paigaldised",
  "Aktuaalsed tehnilised probleemid eriala",
  "Elektervalgustus",
  "PLC kontrollerid",
  "Hoone- ja soojusautomaatika",
  "Mõõteriistade kasutamine testimiseks",
  "Tehniline dokumentatsioon",
  "Rakendusmatemaatika",
  "Projekt",
  "Elektroonika seadmeteremontimine",
  "Heli ja videotehnika",
  "Traadita sidevõrgud",
  "Rakenduselektroonika (praktilised tööd)",
  "IT-halduse standadid",
  "Värvihaldus",
  "Fotograafia",
  "Digitaaltrükk",
  "Multimeedium",
  "Trükikvaliteedi hindamine",
  "Poognamontaaz",
  "Ripi seadistamine ja trükiplaatide valmistamine",
  "Trükkimine",
  "Trükiste kujundamine",
  "Kliendipoolne programmeerimine",
  "Andmebaaside arendamine ja haldus",
  "Serveripoolne programmeerimine",
  "Tunnusgraafika",
  "Videotehnika ja animatsiooni",
  "Filmimine",
  "Toote- ja portreefotod",
  "3Dgraafika",
  "Tükiste järeltöötlus",
  "Zanrid fotograafias",
  "Meistriklass",
  "Illustratsioon",
  "Kujundamine ja küljendamine",
  "Projektijuhtimine praktikas",
  "Sündmusfoto",
  "Portee- ja grupifoto",
  "Analoogfotograafia",
  "Fototehnika",
  "Tootefoto",
  "Kompositsioon",
  "Fototootlus",
  "Mina ja minu tulevik",
  "Suhtlemine ja koostööoskuse arendamine",
  "Ainealse eesti keele oskuse arendamine",
  "Õpioskuste arendamine",
  "Rakendustarkvara",
  "Op. süsteemide alused",
  "Elektrivaldkonna ohutus ja esmaabi",
  "Elektrimootorid ja -ajamid",
  "Aruannete vorm",
  "Elektrimõõtmised",
  "Eesti energiasüsteem",
  "Sisetööde elektriku kutse iseloomustus",
  "Erialase joonestamise alused",
  "SQL",
  "Arvutivõrkude haldus, seadmed ja võrguteenused",
  "Klienditeenindus",
  "Lepingud ja hanked",
  "Kutse-eetika",
  "Rakendusserverite alused",
  "Sissejuhatus õpingutesse",
  "Ohutegurid töökohal",
  "Erinevad hajusrakendused",
  "Agiilne tarkvaraarendus",
  "Tarkvara testimene",
  "Programmeerimine",
  "Projektijuhtimine",
];

const teachers = [
  "Kadri Agu",
  "Liivia Agu",
  "Henry Edward Aimre",
  "Andre Allese",
  "Kristi Arendi",
  "Inga Ausmeel",
  "Anu Baum",
  "Aivo Brenner",
  "Heigo-Aulemb Ensling",
  "Stanislav Huttunen",
  "Nikolai Jumajev",
  "Hurmi Jürjens",
  "Marco Kaare",
  "Kristo Kaasan",
  "Kuldar Kaasik",
  "Ivar Kaljula",
  "Ivar Kaselaid",
  "Hilja Kattago",
  "Kaido Kiil",
  "Tatjana Kirotar",
  "Kevin Otto Koit",
  "Julia Konieva",
  "Villu Kopli",
  "Aleksandr Kormiltsõn",
  "Anna-Liisa Kree",
  "Lea Kreinin",
  "Urmas Krusell",
  "Kairi Kruus",
  "Elena Kudashova",
  "Rutt Kukk",
  "Endrik Kull",
  "Andra Kullerkupp",
  "Siiri Kumari",
  "Tiina-Mae Kuusik",
  "Julia Kähri",
  "Maarja Käsk",
  "Toomas Kästik",
  "Eva-Lotta Künnap",
  "Jaan Lepnurm",
  "Reen Liivat-Oorschot",
  "Üllar Lindmaa",
  "Maris Lindoja",
  "Tiit Ling",
  "Liina Lobjakas",
  "Aleksei Lukašin",
  "Viive Lussmaa",
  "Aare Luup",
  "Erlich Lõwi",
  "Traugott Läänmäe",
  "Ege Meister",
  "Svetlana Mihhailova",
  "Olev Mihkelmaa",
  "Piret Moora",
  "Karl Robert Mägi",
  "Mardo Männimägi",
  "Aleksei Narusberg",
  "Kirill Nelus",
  "Alla Nikitina",
  "Kaupo Nõlvak",
  "Kalle Olumets",
  "Mansur Ongarbayev",
  "Vahur Parve",
  "Ken Peedimaa",
  "Gunnar Peipman",
  "Roman Petrašvili",
  "Karin Plangi",
  "Rain-Julius Plangi",
  "Natalia Popova",
  "Toivo Pärnpuu",
  "Herve Rannu",
  "Pille Raud",
  "Mattias Raun",
  "Pille Reins",
  "Rein Reinstein",
  "Vitali Retšnoi",
  "Mikk Rosin",
  "Terli Rüütli",
  "Reljo Saarepera",
  "Siiri Salin",
  "Heikki Sal-Saller",
  "Jevgeni Sikorski",
  "Tatjana Sinelnik",
  "Triin Sirila",
  "Jaanika Stackhouse",
  "Irina Stassenko",
  "Helena Stern-Kopra",
  "Kaspar Martin Suursalu",
  "Kerim Sütcü",
  "Marina Zotikova",
  "Julia Tammela",
  "Marje Tammert",
  "Inna Tammet",
  "Aivar Teinveld",
  "Anna-Liisa Tiisma",
  "Raivo Timm",
  "Rain Tirul",
  "Timo Triisa",
  "Maksim Tšurkin",
  "Jelizaveta Tšuvpilo",
  "Viljar Tölp",
  "Klea Vaher",
  "Priit Valge",
  "Lembit Vali",
  "Terje Varul",
  "Vadim Veeremaa",
  "Elen Viikmann",
  "Krister Viirsaar",
  "Kertti Viru",
  "Viivika Volt",
  "Elina Õunapuu",
];

const form = reactive({
  first_name: "",
  last_name: "",
  class_name: "",
  subject: "",
  teacher: "",
  rating: "",
  clarity_rating: "",
  participation_rating: "",
  comment: "",
});
const errors = ref({});
const success = ref("");
const saving = ref(false);

async function submitFeedback() {
  errors.value = {};
  success.value = "";
  saving.value = true;

  try {
    const { first_name, last_name, ...feedback } = form;
    const response = await fetch("/api/feedback/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...feedback,
        name: `${first_name.trim()} ${last_name.trim()}`,
        rating: Number(form.rating),
      }),
    });
    const payload = await response.json();
    if (!response.ok) {
      errors.value = payload;
      return;
    }
    Object.assign(form, {
      first_name: "",
      last_name: "",
      class_name: "",
      subject: "",
      teacher: "",
      rating: "",
      clarity_rating: "",
      participation_rating: "",
      comment: "",
    });
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
        <label>Eesnimi<input v-model="form.first_name" type="text" placeholder="Sisesta eesnimi" required /></label>
        <label>Perekonnanimi<input v-model="form.last_name" type="text" placeholder="Sisesta perekonnanimi" required /></label>
      </div>
      <small>{{ errors.name?.[0] }}</small>
      <label>Klass<input v-model="form.class_name" type="text" placeholder="Näiteks 10.B" required /><small>{{ errors.class_name?.[0] }}</small></label>
      <label>Õppeaine<select v-model="form.subject" required><option value="">Vali õppeaine</option><option v-for="subject in subjects" :key="subject" :value="subject">{{ subject }}</option></select><small>{{ errors.subject?.[0] }}</small></label>
      <label>Õpetaja<select v-model="form.teacher" required><option value="">Vali õpetaja</option><option v-for="teacher in teachers" :key="teacher" :value="teacher">{{ teacher }}</option></select><small>{{ errors.teacher?.[0] }}</small></label>
      <fieldset>
        <legend>Üldhinne</legend>
        <p class="muted">1 – väga halb, 5 – väga hea</p>
        <div class="rating"><label v-for="rating in 5" :key="rating"><input v-model="form.rating" type="radio" name="rating" :value="rating" required /> {{ rating }}</label></div>
        <small>{{ errors.rating?.[0] }}</small>
      </fieldset>
      <fieldset>
        <legend>Kui arusaadavad olid tunnid õppeaasta jooksul?</legend>
        <p class="muted">1 – üldse mitte arusaadavad, 5 – väga arusaadavad</p>
        <div class="rating"><label v-for="rating in 5" :key="rating"><input v-model="form.clarity_rating" type="radio" name="clarity_rating" :value="rating" required /> {{ rating }}</label></div>
        <small>{{ errors.clarity_rating?.[0] }}</small>
      </fieldset>
      <fieldset>
        <legend>Kas said tunnis piisavalt kaasa rääkida?</legend>
        <p class="muted">1 – üldse mitte, 5 – väga palju</p>
        <div class="rating"><label v-for="rating in 5" :key="rating"><input v-model="form.participation_rating" type="radio" name="participation_rating" :value="rating" required /> {{ rating }}</label></div>
        <small>{{ errors.participation_rating?.[0] }}</small>
      </fieldset>
      <label>Kommentaar <span>(valikuline)</span><textarea v-model="form.comment" maxlength="500" placeholder="Kirjuta soovi korral kommentaar..." /><small>{{ errors.comment?.[0] }}</small></label>
      <button type="submit" :disabled="saving">{{ saving ? "Salvestan..." : "Saada tagasiside" }}</button>
      <p v-if="success" class="success">{{ success }}</p>
      <p v-if="errors.non_field_errors" class="error">{{ errors.non_field_errors[0] }}</p>
    </form>
  </section>
</template>
