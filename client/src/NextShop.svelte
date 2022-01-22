<script>
    import SuggestionsCell from "./SuggestionsCell.svelte";
    import { slide, scale } from 'svelte/transition';
    import { push } from 'svelte-spa-router';

    let isExpanded = false;

    function toggle(){
        isExpanded = !isExpanded;
    }

    let suggestions = [
        {
            locationName: "Sainsbury's Local",
            locationType: "sains",
            estimatedPrice: 16.06,
            distance: 0.50,
            isOnline: false,
        },
        {
            locationName: "Ocado",
            locationType: "ocado",
            estimatedPrice: 18.90,
            deliveryDate: "23/Jan/2022",
            isOnline: true,
        },
        {
            locationName: "Tesco",
            locationType: "tesco",
            estimatedPrice: 17.06,
            distance: 1.0,
            isOnline: false,
        },
    ]

    $: topSuggestion = suggestions[0];

    let items = [
        {name: "Apples", quantity: 2}
    ]

    function changeForKey(key, change)
    {
        // TODO (ti250): if the quantity for the key goes to 0, then delete
        function changeForKeyInternal()
        {
            let item = items.find((element) => element.name == key);
            item.quantity += change;
            if (item.quantity <= 0)
            {
                const index = items.indexOf(item);
                items.splice(index, 1);
            }
            items = items;
        }
        return changeForKeyInternal;
    }

    function onItemNameKeyDown(event) {
        console.log("onItemKeyDown");
        if (event.keyCode == 13 && nextItemName !== "") {
            console.log("onItemKeyDown");
            addItem();
        }
    }

    function addItem() {
        console.log("addItem Called");
        items.push({name: nextItemName, quantity: 1});
        nextItemName = "";
    }

    let nextItemName="";
</script>

<div id="content" in:scale>
    <button onclick="window.history.back()">
    &lt; Back
    </button>

    <h1>
        My Next Shop
    </h1>

    <!-- Default suggestion -->
    <div class="suggestion">
        <SuggestionsCell cellData={topSuggestion}/>
    </div>

    {#if isExpanded}
        <div transition:slide>
            {#each suggestions.slice(1) as suggestion}
                <div class="suggestion">
                    <SuggestionsCell cellData={suggestion}/>
                </div>
            {/each}
        </div>
    {/if}

    <button on:click={toggle} id="expandButton" class="decorated"> <span> {isExpanded ? "▲ Show Less" : "▼ Show More"} </span> </button>
    <br/>

    {#each items as item (item.name)}
        <div class="itemCell">
            <div>
                ・{item.name}
            </div>
            <div class="quantityManager">
                {item.quantity}
                <div class="quantityButtons">
                    <button class="quantityButton" on:click={changeForKey(item.name, 1)}>▲</button>
                    <button class="quantityButton" on:click={changeForKey(item.name, -1)}>▼</button>
                </div>
            </div>
        </div>
    {/each}
    <br/>
    <input class="nextItemInput" placeholder="Add an Item" on:keydown={onItemNameKeyDown} bind:value={nextItemName}>
</div>
<button class="floatingActionButton" on:click={() => push('/scanReceipt')}>
    I did a shop!
</button>

<style>
    button {
        background: none;
        border: none;
    }

    #content {
        padding: 10px;
    }

    #expandButton {
        width: 100%;
        border: none;
        background: none;
    }

    .suggestion {
        margin-bottom: 10px;
    }

    .nextItemInput {
        width: 100%;
    }

    .itemCell {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 5px;
    }

    .quantityManager {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-end;
    }

    .quantityButtons {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-left: 10px;
        /*width: 30px;*/
    }

    .quantityButton {
        height: 20px;
        padding: 0px;
        margin: 0px;
    }

    .floatingActionButton {
        position: fixed;
        bottom: 50px;
        right: 20px;
        z-index: 999;
        background: lightgrey;
        border-radius: 40px;
        padding: 20px;
    }

    /* headlines with lines from https://stackoverflow.com/questions/15557627/heading-with-horizontal-line-on-either-side */
    .decorated{
         overflow: hidden;
         text-align: center;
     }
    .decorated > span{
        position: relative;
        display: inline-block;
    }
    .decorated > span:before, .decorated > span:after{
        content: '';
        position: absolute;
        top: 50%;
        border-bottom: 1px solid;
        width: 100vw;
        margin: 0 15px;
    }
    .decorated > span:before{
        right: 95%;
    }
    .decorated > span:after{
        left: 95%;
    }
</style>
