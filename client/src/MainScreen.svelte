<script>
    import Card from "./Card.svelte";
    import { push } from 'svelte-spa-router';
    import { suggestions, pastShops } from './store';

    let currentShop = {
        itemNames: ["Water", "Chicken"], // Names of things in the shopping list
        estimatedCost: 16.06, // Total cost in pounds
        suggestedLocation: "Sainsbury's Local", // Location Name
        suggestedLocationType: "sains", // We can use this to maybe show a favicon later next to the location name
    }

    $: topSuggestion = ($suggestions)[0]

    // let pastShops = [
    //     {
    //         locationName: "Sainsbury's Local",
    //         cost: 12.05,
    //         locationType: "sains",
    //         date: "23/Jan"
    //     },
    //     {
    //         locationName: "Tesco Express",
    //         cost: 13.20,
    //         locationType: "tesco",
    //         date: "17/Jan"
    //     },
    //     {
    //         locationName: "Waitrose",
    //         cost: 15.20,
    //         locationType: "waitrose",
    //         date: "12/Jan"
    //     },
    // ]
</script>

<div id="content">
    <!-- Title element -->
    <h1>
        My Shop List
    </h1>

<hr>

    <!-- Next Shop -->
    <h2>
        My Next Shop
    </h2>
    <div class="listElement" on:click={() => push('/nextShop')}>
        <Card isFloating="true" backgroundColor="PeachPuff">
            <div class="cardContent">
                <div class="estimateCardContent">
                    <div class="supermarketDescription">
                        <img src={"/supermarketFavicons/" + topSuggestion.locationType + ".png"} class="supermarketFavicon"/>
                        <div>
                            {topSuggestion.locationName}
                        </div>
                    </div>
                    <div id="costEstimate">
                        Estimate:
                        <br/>
                        £{topSuggestion.estimatedPrice.toFixed(2)}
                    </div>
                </div>
            </div>
        </Card>
    </div>

    <br/>
        <h2>
            My Shop History
        </h2>

    {#each $pastShops as pastShop}
        <div class="listElement pastShop">
            <Card backgroundColor="WhiteSmoke">
                <div class="cardContent">
                    <div class="estimateCardContent">
                        <div class="supermarketDescription hist">
                        <img src={"/supermarketFavicons/" + pastShop.locationType + ".png"} class="supermarketFavicon"/>
                        <div class="hist">
                            {pastShop.locationName}
                        </div>
                        </div>
                        <div class="date hist">
                            Date:
                            <br/>
                            {pastShop.date}
                        </div>
                        <div class="costEstimate hist">
                            Cost:
                            <br/>
                            £{pastShop.cost.toFixed(2)}
                        </div>
                    </div>
                </div>
            </Card>
        </div>
    {/each}
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <button class="floatingActionButton" on:click={() => push('/scanReceipt')}>
        I did a shop!
    </button>
</div>

<style>
    h1 {
        margin-left: 8px;
        text-align: left-align;
        font-weight: 700;
    }

    h2 {
        margin-left: 8px;
        text-align: left-align;
    }

    hr {
        border: 1px solid lightgray;
    }

    #content {
        padding: 20px;
    }

    .supermarketFavicon {
        margin-right: 15px;
        border-radius: 5px;
        overflow: hidden;
        width: 20px;
        height: 20px;
    }

    .estimateCardContent {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }

    .supermarketDescription {
        display: flex;
        flex-direction: row;
        /*justify-content: space-between;*/
        align-items: center;
    }

    .date{
    text-align: left;
    position:absolute; 
    left:195px; 
    top:21px
    }

    .costEstimate{
        text-align: right;
    }

    .hist{
        color: Gray
    }


    .floatingActionButton {
        position: fixed;
        bottom: 50px;
        right: 20px;
        z-index: 999;
        background: SandyBrown;
        color: White;
        border-radius: 40px;
        border-color: rgba(0, 0, 0, 0);
        padding: 20px;
    }

    .cardContent {
        margin: 20px;
    }

    .listElement{
        margin-top: 10px;
        cursor: pointer;
    }

    .pastShop{
        transform: scale(0.95);
    }
</style>
