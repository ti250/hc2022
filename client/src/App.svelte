<script>
    import Router from 'svelte-spa-router';
    import RandomView from './RandomView.svelte';
    import RandomView2 from './RandomView2.svelte';
    import MainScreen from './MainScreen.svelte';
    import NextShop from './NextShop.svelte';
    import ReceiptScanningView from './ReceiptScanningView.svelte';
    import ReceiptFeedbackView from './ReceiptFeedbackView.svelte';


    const routes = {
        '/': MainScreen,
        '/nextShop': NextShop,
        '/scanReceipt': ReceiptScanningView,
        '/receiptFeedback': ReceiptFeedbackView,
        '/randomView2': RandomView2,
    }
</script>

<body>
    <Router {routes}/>
</body>
