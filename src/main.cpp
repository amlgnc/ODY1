#include <SFML/Audio.hpp>
#include <SFML/Graphics.hpp>

int main()
{
    sf::RenderWindow window(sf::VideoMode(800, 600), "ODY1");

    sf::Texture texture;
    if (!texture.loadFromFile("SFML/bin/test.jpg"))
        return EXIT_FAILURE;
    sf::Sprite sprite(texture);

    sf::Font font;
    if (!font.loadFromFile("SFML/bin/test.ttf"))
        return EXIT_FAILURE;
    sf::Text text("Yay!", font, 50);

    sf::Music music;
    if (!music.openFromFile("SFML/bin/test.ogg"))
        return EXIT_FAILURE;
    // music.play();

    // Main loop
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            // Close window: exit
            if (event.type == sf::Event::Closed)
                window.close();
        }
        window.clear();
        window.draw(sprite);
        window.draw(text);
        window.display();
    }
    return EXIT_SUCCESS;
}