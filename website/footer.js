(() => {
  const AUTHOR_NAME = 'Mahsa Keikha';
  const AUTHOR_URL = 'https://github.com/MahsaKeikha';

  function addAuthorAttribution() {
    document.querySelectorAll('footer').forEach((footer) => {
      let attribution = footer.querySelector('.footer-attribution');
      if (!attribution) {
        attribution = document.createElement('p');
        attribution.className = 'footer-attribution';
        footer.insertBefore(attribution, footer.firstChild);
      }

      attribution.replaceChildren(
        document.createTextNode('Research by '),
      );
      const author = document.createElement('a');
      author.href = AUTHOR_URL;
      author.textContent = AUTHOR_NAME;
      author.rel = 'author';
      attribution.append(author, document.createTextNode(' · Mathematical Consciousness Bridge'));
    });
  }

  document.addEventListener('DOMContentLoaded', addAuthorAttribution);
})();