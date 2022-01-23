<script>
    import SuggestionsCell from "./SuggestionsCell.svelte";
    import { slide, scale } from 'svelte/transition';
    import { push } from 'svelte-spa-router';
    import { suggestions, items } from './store';

    let isExpanded = false;
    let newNames = [];

    function toggle(){
        isExpanded = !isExpanded;
    }

    $: topSuggestion = ($suggestions)[0];
    console.log($suggestions[0]);

    // let items = [
    //     {name: "Apples", quantity: 2}
    // ]

    function changeForKey(key, change)
    {
        function changeForKeyInternal()
        {
            let localItems = $items
            let item = localItems.find((element) => element.name == key);
            item.quantity += change;
            if (item.quantity <= 0)
            {
                const index = localItems.indexOf(item);
                localItems.splice(index, 1);
            }
            items.set(localItems);
            localStorage.setItem("items", JSON.stringify($items));
            onItemsChange();
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
        let localItems = $items;
        localItems.push({name: nextItemName, quantity: 1});
        items.set(localItems);
        localStorage.setItem("items", JSON.stringify($items));
        onItemsChange();
        nextItemName = "";
    }

    async function onItemsChange() {
        let url = "./api/supermarket_recommendations";
        let requestBody = {
            quantities: $items,
            location: {
                latitude: 52.20483,
                longitude: 0.11972,
            }
        }
        let requestParameters = {method: "POST", body: JSON.stringify(requestBody)};
        const res = await fetch(url, requestParameters);
        const newData = await res.json();
        console.log(newData);
        suggestions.set(newData.recommendations);
        localStorage.setItem("suggestions", JSON.stringify($suggestions));
        newNames = newData.newNames;
    }

    let nextItemName="";
    onItemsChange();
</script>

<div id="content" in:scale>
    <button onclick="window.history.back()" id="backbutton">
    &lt; Back
    </button>
    <h1>
        My Next Shop
    </h1>

    <hr>

    <!-- Default suggestion -->
    <h2>
        Cheapest in your vicinity
    </h2>
    <div class="suggestion">
        <SuggestionsCell cellData={topSuggestion}/>
    </div>

    {#if isExpanded}
        <div transition:slide>
            {#each ($suggestions).slice(1) as suggestion}
                <div class="suggestion">
                    <SuggestionsCell cellData={suggestion}/>
                </div>
            {/each}
        </div>
    {/if}

    <button on:click={toggle} id="expandButton" class="decorated"> <span> {isExpanded ? "▲ Show Less Store Options" : "▼ Show More Store Options"} </span> </button>
    <br/>

    <br>
    <br>

    <h2>
        Items in the basket
    </h2>
    {#each $items as item (item.name)}
        <div class="itemCell">
            <div>
                {#if newNames.includes(item.name.toLowerCase())}
                    ? {item.name}
                {:else}
                    {item.name}
                {/if}
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
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
</div>
<button class="floatingActionButton" on:click={() => push('/scanReceipt')}>
    I did a shop!
</button>

<style>
    h1 {
        margin-left: 8px;
        text-align: left-align;
        font-weight: 700;
    }

    h2 {
        text-align: left-align;
    }

    hr {
        border: 1px solid lightgray;
    }

    #backbutton {
        padding: 0px;
        margin-bottom: 10px;
        color: SandyBrown;
    }

    button {
        background: none;
        border: none;
        margin: 0px;
    }

    #content {
        padding: 20px;
    }

    #expandButton {
        width: 100%;
        border: none;
        background: none;
        color: SandyBrown;
    }

    .suggestion {
        margin-bottom: 20px;
        margin-left: 10px;
        margin-right: 10px;
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
        background: SandyBrown;
        color: White;
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
