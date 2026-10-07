<template>
  <header class="site-header">
    <div class="container nav">
      <RouterLink class="brand" to="/tagasiside">Õppeainete tagasiside</RouterLink>
      <nav aria-label="Peamine navigatsioon">
        <RouterLink to="/tagasiside">Tagasiside</RouterLink>
        <RouterLink to="/ulevaade">Ülevaade</RouterLink>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <span class="badge">Õpilase tagasiside</span>
      <h1>Aita meil õppeaineid paremaks muuta.</h1>
      <p>Anna läbitud õppeainele hinne ja soovi korral lisa kommentaar.</p>
    </section>
    <RouterView />
  </main>

  <footer>
    <div class="container">Õppeainete tagasiside rakendus</div>
  </footer>
</template>
