<script>
    import { push } from 'svelte-spa-router';
    import { scale } from 'svelte/transition';
    import { feedback } from './store';
</script>

<div id="content" in:scale>
    <h1>
        Thank You for Your Contribution!
    </h1>
    You spent £{$feedback.actualTotal.toFixed(2)} at
    <img src={"/supermarketFavicons/" + $feedback.locationType + ".png"} class="supermarketFavicon"/> {$feedback.locationName}
    <h2>
        Here's some estimates of what you would have spent at other places:
    </h2>
    {#each $feedback.feedback as feedbackItem}
        <div class="feedbackItem">
            <div>
                <img src={"/supermarketFavicons/" + feedbackItem.locationType + ".png"} class="supermarketFavicon"/> {feedbackItem.name}
            </div>
            <div>
                £{feedbackItem.predictedPrice.toFixed(2)}
            </div>
        </div>
    {/each}
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

    .supermarketFavicon {
        margin-right: 15px;
        border-radius: 5px;
        overflow: hidden;
        width: 20px;
        height: 20px;
    }

    .feedbackItem {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
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
