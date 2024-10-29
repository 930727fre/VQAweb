<template>
    <main class="flex flex-col">
        <section data-layername="layout" class="flex overflow-hidden flex-col w-full bg-white max-md:max-w-full">
            <div data-layername="bb" class="flex flex-col px-10 pt-6 pb-11 w-full bg-pink-100 max-md:px-5 max-md:max-w-full">
                <article data-layername="background" class="flex flex-col pb-11 rounded-xl bg-gray-300 bg-opacity-50 shadow-[8px_8px_20px_rgba(0,0,0,0.25)] max-md:max-w-full">
                    <header data-layername="top" class="flex flex-col items-center px-20 rounded-xl bg-slate-500 bg-opacity-80 max-md:px-5 max-md:max-w-full">
                        <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/b7a590f92b1f65a24ce07a05473b37fdc1b29cc5729fff5e9a9b073888d5dac0?placeholderIfAbsent=true&apiKey=c9bff0a3a0134cf2b1616c259a379779" alt="Header image" class="object-contain z-10 -mt-6 mb-0 w-60 max-w-full aspect-[1.21] max-md:mb-2.5" />
                    </header>
                    <div data-layername="qOutput" class="flex shrink-0 self-end mt-14 mr-28 max-w-full bg-rose-400 rounded-xl h-[196px] w-[567px] max-md:mt-10 max-md:mr-2.5"></div>
                    <div class="flex flex-col mt-4 ml-11 w-full max-w-[1653px] max-md:max-w-full">
                        <div class="flex flex-wrap gap-5 self-start">
                            <img loading="lazy" src="https://cdn.builder.io/api/v1/image/assets/TEMP/b7c332c3f99892b74d78c990544d2a91866a93b2f9283bab2ceef1019cdd0e19?placeholderIfAbsent=true&apiKey=c9bff0a3a0134cf2b1616c259a379779" alt="User avatar" class="object-contain shrink-0 my-auto aspect-square shadow-[0px_4px_4px_rgba(0,0,0,0.25)] w-[74px]" />
                            <div data-layername="aOutput" class="flex shrink-0 max-w-full bg-rose-200 rounded-xl h-[196px] w-[567px]"></div>
                        </div>
                        <div class="flex flex-wrap self-end mt-64 w-full text-2xl text-white max-w-[1551px] max-md:mt-10 max-md:max-w-full">
                            <button data-layername="picInput" class="px-8 py-7 rounded-xl bg-slate-500 max-md:px-5 max-md:max-w-full" @click="handleUpload">
                            Upload the picture
                        </button>
                        <div data-layername="mid" class="flex shrink-0 bg-sky-900 h-[81px] w-[51px]"></div>
                        <form @submit.prevent="handleSubmit" class="flex-grow">
                        <label for="questionInput" class="sr-only">Type your Question</label>
                        <input
                            id="questionInput"
                            type="text"
                            v-model="question"
                            placeholder="Type your Question"
                            class="px-7 py-8 rounded-none bg-slate-500 w-full max-md:px-5 max-md:max-w-full"
                        />
                    </form>
            </div>
        </div>
    </article>
</div>
    </section >
  </main >
</template >

    <script lang="ts">
        import {defineComponent, ref} from 'vue';

        export default defineComponent({
            name: 'ImageUploadQuestion',
        setup() {
    const question = ref('');

    const handleUpload = () => {
            // Implement image upload logic here
        };

    const handleSubmit = () => {
            // Implement question submission logic here
        };

        return {
            question,
            handleUpload,
            handleSubmit,
    };
  },
});
    </script>
