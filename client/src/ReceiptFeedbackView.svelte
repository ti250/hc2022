<script>
    import { push } from 'svelte-spa-router';
    import { scale } from 'svelte/transition';
    import { feedback } from './store';

    function color(feedbackItem){
        if ($feedback.actualTotal > feedbackItem.predictedPrice) {
                return "red"
        }
        else {
                return "black"
        }
    }
</script>

<div id="content" in:scale>
    <h1>
        Thank You for Your Contribution!
    </h1>
    <div class = "amountSpent">
        You spent <strong><span style="color:blue">£{$feedback.actualTotal.toFixed(2)} </span></strong> at
        <img src={"/supermarketFavicons/" + $feedback.locationType + ".png"} class="supermarketFavicon inline"/> {$feedback.locationName}
    </div>
    <hr>
    <h3>
        Here are the alternative options you had:
    </h3>
    {#each $feedback.feedback as feedbackItem}
            <div class="feedbackItem">
                <div>
                    <img src={"/supermarketFavicons/" + feedbackItem.locationType + ".png"} class="supermarketFavicon"/> {feedbackItem.name}
                </div>
                <div>
                    <span style="color:{color(feedbackItem)}">
                        £{feedbackItem.predictedPrice.toFixed(2)}
                    </span>
                </div>
            </div>
    {/each}
    <button on:click={() => push('/')} id="backbutton">
        &lt; Back
    </button>
</div>

<style>
    
    h1 {
        margin-left: 8px;
        text-align: left-align;
        font-weight: 700;
    }

    h3 {
        margin-top: 100px;
        text-align: left-align;
        font-weight: 700;
    }

    .supermarketFavicon {
        margin-right: 15px;
        border-radius: 5px;
        overflow: hidden;
        width: 20px;
        height: 20px;
    }

    .inline {
        margin-right: 0px;
    }

    .feedbackItem {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }

    .amountSpent{
        text-align: center;
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
