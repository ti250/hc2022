<script>
    import Router from 'svelte-spa-router';
    import RandomView from './RandomView.svelte';
    import RandomView2 from './RandomView2.svelte';
    import MainScreen from './MainScreen.svelte';
    import NextShop from './NextShop.svelte';


    const routes = {
        '/': MainScreen,
        '/nextShop': NextShop,
        '/randomView2': RandomView2,
    }
</script>

<body>
    <Router {routes}/>
</body>
