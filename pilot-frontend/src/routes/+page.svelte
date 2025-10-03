<script>
  import HomePage from '$lib/components/HomePage.svelte';

  let { data } = $props();

  const page = $derived(data.page);
</script>

<svelte:head>
  <title>{page?.title || 'Home'}</title>
  {#if page?.meta_description}
    <meta name="description" content={page.meta_description} />
  {/if}
</svelte:head>

<HomePage {page} />