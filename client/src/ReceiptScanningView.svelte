<!-- Essentially https://dev.to/nelsoncode/how-to-use-the-webcam-with-svelte-js-2415 -->
<script>
    let videoSource = null;
    let loading = false;

    const getCamera = async () => {
        try {
            loading = true;
            const stream = await navigator.mediaDevices.getUserMedia({
                video: true,
            });
            videoSource.srcObject = stream;
            videoSource.play();
            loading = false;
        } catch (error) {
            console.log(error);
        }
    };
</script>

<div>
    {#if loading}
        <h1>Loading...</h1>
    {/if}
    <video bind:this={videoSource} />
    <button on:click={getCamera}>CLICK</button>
</div>
