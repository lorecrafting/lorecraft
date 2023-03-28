<script>
  import { afterUpdate } from "svelte";
  import { Popover } from "sveltestrap";

  let name;
  let desc;
  let contents = [];
  let characters = [];
  let exits = [];
  let formInput;
  let echoLogs = [];
  let scrollableDiv;

  afterUpdate(() => {
    scrollableDiv.scrollTo(0, scrollableDiv.scrollHeight);
  });

  function handleWindowLoad() {
    Evennia.init();
    window.Evennia.emitter.on("room_data", function (empty, roomData) {
      name = roomData.name;
      desc = roomData.desc;
      contents = roomData.contents;
      characters = _formatCharacters(roomData.characters);
      exits = roomData.exits.filter((exit) => {
        return (
          exit === "north" ||
          exit === "south" ||
          exit === "east" ||
          exit === "west"
        );
      });
    });
    window.Evennia.emitter.on("text", function (text, cmd) {
      if (cmd.type === "look") {
        return;
      }
      echoLogs = [...echoLogs, text[0]];
    });
  }

  function handleClickTitle() {
    Evennia.msg("text", ["look"]);
    echoLogs = [];
  }

  function onSubmit(e) {
    Evennia.msg("text", [formInput]);
    formInput = "";
  }

  function evenniaMsg(str) {
    Evennia.msg("text", [str])
  }

  function handleClickExit(exit) {
    Evennia.msg("text", [exit]);
    echoLogs = [];
  }

  function _formatCharacters(characters) {
    let str;

    if (characters.length === 1) {
      return _upcaseFirstChar(`${characters[0]} is here.`);
    }
    if (characters.length === 2) {
      return _upcaseFirstChar(
        `${characters[0]} and ${characters[1]} are here.`
      );
    }
    if (characters.length > 2) {
      let lastChar = characters.pop();
      return _upcaseFirstChar(
        `${characters.join(", ")}, and ${lastChar} are here.`
      );
    }
  }

  function _upcaseFirstChar(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }
</script>

<svelte:window on:load={handleWindowLoad} />

<main>
  <section class="room-info">
    <h1 on:click={handleClickTitle}>{name}</h1>
    <p>{@html desc}</p>
    <p>
      {#if contents}
        {#if contents.length === 1}
          <div>You see <span id={contents[0] + "0"}>a {contents[0]}.</span></div>
          <Popover target={contents[0] + "0"}
            ><div on:click={()=> evenniaMsg(`look ${contents[0]}`)}>look</div>
            <div on:click={()=> evenniaMsg(`get ${contents[0]}`)}>get</div></Popover
          >
        {/if}
        {#if contents.length === 2}
          <div>
            You see <span id={contents[0] + "0"}>a {contents[0]}</span> and
            <span id={contents[1] + "1"}>a {contents[1]}.</span>
          </div>
          <Popover target={contents[0] + "0"}>
            <div on:click={()=> evenniaMsg(`look ${contents[0]}`)}>look</div>
            <div on:click={()=> evenniaMsg(`get ${contents[0]}`)}>get</div>
          </Popover>
          <Popover target={contents[1] + "1"}>
            <div on:click={()=> evenniaMsg(`look ${contents[1]}`)}>look</div>
            <div on:click={()=> evenniaMsg(`look ${contents[1]}`)}>get</div>
          </Popover>
        {/if}
        {#if contents.length > 2}
          <div>
            You see <span id={contents[0] + "0"}> a {contents[0]},</span>
            {#each contents as item, i}
              {#if i > 0 && i < contents.length - 1}
                <span id={item + i}>a {contents[i]}</span>
                <Popover target={item + i}>
                  <div on:click={()=> evenniaMsg(`look ${item}`)}>look</div>
                  <div on:click={()=> evenniaMsg(`get ${item}`)}>get</div>
                </Popover>
              {/if}
            {/each}
            <span id={contents[contents.length - 1]}
              >and a {contents[contents.length - 1]}.
            </span>
            {#if characters}
              <span>{characters}</span>
            {/if}
          </div>
          <Popover target={contents[0] + "0"}>
            <div on:click={()=> evenniaMsg(`look ${contents[0]}`)}>look</div>
            <div on:click={()=> evenniaMsg(`get ${contents[0]}`)}>get</div>
          </Popover>
          <Popover target={contents[contents.length - 1]}>
            <div on:click={()=> evenniaMsg(`look ${contents[contents.length-1]}`)}>look</div>
            <div on:click={()=> evenniaMsg(`look ${contents[contents.length-1]}`)}>get</div>
          </Popover>
        {/if}
      {/if}
    </p>

    <p>
      {#if exits.length > 0}
        You can go
      {/if}
      {#each exits as exit}
        <button on:click={() => handleClickExit(exit)}>{exit}</button><span
          >&nbsp;</span
        >
      {/each}
    </p>
  </section>

  <section bind:this={scrollableDiv} class="echo-log">
    {#each echoLogs as exit}
      <p>{@html exit}</p>
    {/each}
  </section>

  <form class="form-input" on:submit|preventDefault={onSubmit}>
    <input bind:value={formInput} type="text" />
  </form>
</main>

<style>
  main {
    text-align: center;
    padding: 2em;
    margin: 0 auto;
    line-height: 1.5rem;
    display: flex;
    flex-direction: column;
    height: 89vh;
    overflow: hidden;
  }

  .room-info {
    flex: 0 0 auto;
  }

  .echo-log {
    flex: 1 1 auto;
    overflow-y: scroll;
    margin-right: -60px;
    padding-right: 40px;
    scroll-behavior: smooth;
  }

  .form-input {
    flex: 0 0 auto;
  }

  input {
    width: 100%;
  }

  p {
    text-align: left;
    word-wrap: break-word;
  }

  p::first-letter {
    text-transform: capitalize;
  }

  h1 {
    text-transform: uppercase;
    font-size: 3em;
    font-weight: 100;
    margin-bottom: 2rem;
  }

  button {
    text-decoration: underline;
    background-color: transparent;
    border-width: 0;
    font-family: inherit;
    font-size: inherit;
    font-style: inherit;
    font-weight: inherit;
    line-height: inherit;
    padding: 0;
  }
  button:hover {
    cursor: pointer;
    color: rgb(255, 183, 183);
    text-decoration: underline;
  }
</style>
