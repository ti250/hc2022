<!-- Essentially https://dev.to/nelsoncode/how-to-use-the-webcam-with-svelte-js-2415 -->
<script>
    import { push } from 'svelte-spa-router';
    import { scale } from 'svelte/transition';

    let videoSource = null;
    let loading = false;

    const getCamera = async () => {
        try {
            loading = true;
            const stream = await navigator.mediaDevices.getUserMedia({
                // video: true,
                video: { facingMode: "environment" }
            });
            videoSource.srcObject = stream;
            videoSource.play();
            loading = false;
        } catch (error) {
            console.log(error);
        }
    };

    getCamera();

    function takePhoto() {
        console.log("Take Photo Called");
        push("/receiptFeedback");
    }
</script>

<div id="content" in:scale>
    <button onclick="window.history.back()" id="backbutton">
        &lt; Back
    </button>
    {#if loading}
        <h1>Loading...</h1>
    {/if}
    <video id="cameraView" bind:this={videoSource} playsinline />
    <div class="photo-button">
        <button on:click={takePhoto} class="photo-button">
        </button>
    </div>

</div>

<style>
    
    h1 {
        text-align: center;
        font-weight: 700;
    }

    #backbutton {
        border-color: white;
        padding: 20px;
        margin: 20px;
        color: SandyBrown;
        border-radius: 40px;
        padding: 20px;
    }

    #content {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: black;
        color: white;
    }

    #cameraView {
        width: 95%;
        position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%);
        border-radius: 20px;
    }

    .photo-button {
      width: 100px;
      height: 100px;
      top: 85%;
      left: 50%;
      margin-top: -50px;
      margin-left: -50px;
      position: absolute;
      border-radius: 100%;
    }

</style>
