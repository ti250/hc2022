<script>
    import { push } from 'svelte-spa-router';
</script>

<div id="content">
    <h1>
        Thank You!
    </h1>
    <h1>
        Our robot helpers are busy updating our database....
    </h1>
    <div id="backButtonWrapper">
        <button on:click={() => push('/')} id="backButton">Back</button>
    </div>
</div>

<style>
    #content {
        margin: 30px;
    }

    #backbutton {
        width: 100%;
    }

    #backButtonWrapper {
        position: absolute;
        bottom: 100px;
        left: 0px;
        width: 100%;
        z-index: 999;

        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }
</style>
