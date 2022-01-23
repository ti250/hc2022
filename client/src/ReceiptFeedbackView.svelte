<script>
    import { push } from 'svelte-spa-router';
</script>

<div id="content" in:scale>
    <h1>
        Thank You for Your Contribution!
    </h1>
    <h2>
        Our robot helpers are updating our database for the next user!
    </h2>
        <button on:click={() => push('/')} id="backbutton">
            &lt; Back
        </button>
</div>

<style>
    
    h1 {
    text-align: center;
    font-weight: 700;
    }

    h2 {
    margin-top: 100px;
    text-align: center;
    font-weight: 700;
    }

    #content {
        margin: 30px;
    }

    #backbutton {
        position: fixed;
        bottom: 50px;
        left: 20px;
        z-index: 999;
        background: SandyBrown;
        color: White;
        border-radius: 40px;
        padding: 20px;
    }

</style>
