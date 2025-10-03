<script>
  import '../styles/global.css';
  import Header from '$lib/components/Header.svelte';
  import Footer from '$lib/components/Footer.svelte';
  import Navigation from '$lib/components/Navigation.svelte';

  let { data, children } = $props();
  // console.log('Layout data:', data);

</script>

<div class="app">
  <Header />
  <Navigation navigationMenus={data.navigationMenus} />
  <main>
    {@render children()}
  </main>
  <Footer />
</div>

<style>
  :global(body) {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
    color: #333;
  }

  .app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  main {
    flex: 1;
  }

  :global(a) {
    color: #0066cc;
    text-decoration: none;
  }

  :global(a:hover) {
    text-decoration: underline;
  }
</style>