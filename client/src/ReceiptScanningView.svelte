<!-- Essentially https://dev.to/nelsoncode/how-to-use-the-webcam-with-svelte-js-2415 -->
<script>
    import { push } from 'svelte-spa-router';
    import { scale } from 'svelte/transition';

    let videoSource = null;
    let loading = false;
    const scratchCanvas = document.createElement('canvas');

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
        scratchCanvas.width = videoSource.videoWidth;
        scratchCanvas.height = videoSource.videoHeight;
        const scratchContext = scratchCanvas.getContext('2d');
        scratchContext.drawImage(videoSource, 0, 0, videoSource.videoWidth, videoSource.videoHeight);
        scratchCanvas.toBlob(
            function (jpegBlob) {
                const formData = new FormData();
                formData.append("photo", jpegBlob);

                fetch("/api/analyse_receipt",
                {
                    method: "POST",
                    body: formData
                })
                .then(response => {
                    return response.json();
                })
                .then(jsonified => {
                    console.log(jsonified);
                })
                .then(() => {
                    push("/receiptFeedback");
                })
            }, 'image/jpeg'
        )
    }
</script>

<div id="content" in:scale>
    <video id="cameraView" bind:this={videoSource} playsinline />
    <div>
        <button onclick="window.history.back()" id="backbutton">
            &lt; Back
        </button>
    </div>
    {#if loading}
        <h1>Loading...</h1>
    {/if}
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
        position:  absolute;
        border-color: white;
        padding: 20px;
        margin: 20px;
        color: SandyBrown;
        border-radius: 40px;
        padding: 20px;
        z-index: 100;
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
