<script>
    import Router from 'svelte-spa-router';
    import RandomView from './RandomView.svelte'
    import RandomView2 from './RandomView2.svelte'

    const routes = {
        '/': RandomView,
        '/randomView2': RandomView2,
    }
</script>

<body>
    <Router {routes}/>
</body>
