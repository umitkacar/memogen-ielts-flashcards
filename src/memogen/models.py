"""Data models for MEMOGEN vocabulary system."""

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class DifficultyLevel(str, Enum):
    """IELTS difficulty levels."""

    EASY = "easy"
    MEDIUM = "medium"
    DIFFICULT = "difficult"


class VocabularyCard(BaseModel):
    """Model for a single vocabulary flashcard.

    Attributes:
        word: The vocabulary word
        pronunciation: Phonetic pronunciation
        pos: Part of speech (noun, verb, adjective, etc.)
        definition: Clear, concise definition
        example: Example sentence showing usage
        synonyms: Comma-separated list of synonyms
        level: Difficulty level (easy, medium, difficult)
        emoji: Visual emoji representation
        image_url: Optional URL to associated image
        ielts_band: IELTS band score range (e.g., "4-5", "6-7", "8-9")
    """

    word: str = Field(..., min_length=1, description="The vocabulary word")
    pronunciation: str = Field(..., description="Phonetic pronunciation")
    pos: str = Field(..., description="Part of speech")
    definition: str = Field(..., min_length=1, description="Word definition")
    example: str = Field(..., min_length=1, description="Example sentence")
    synonyms: str = Field(..., description="Comma-separated synonyms")
    level: DifficultyLevel = Field(..., description="Difficulty level")
    emoji: str = Field(default="📚", description="Visual emoji")
    image_url: Optional[str] = Field(None, description="Image URL")
    ielts_band: str = Field(..., description="IELTS band score range")

    class Config:
        """Pydantic model configuration."""

        json_schema_extra = {
            "example": {
                "word": "ABUNDANT",
                "pronunciation": "/əˈbʌndənt/",
                "pos": "adjective",
                "definition": "Available in large quantities; plentiful",
                "example": "The forest has abundant wildlife and natural resources.",
                "synonyms": "plentiful, copious, ample, profuse",
                "level": "easy",
                "emoji": "🌾",
                "ielts_band": "4-5",
            }
        }


class VocabularyDeck(BaseModel):
    """Model for a collection of vocabulary cards.

    Attributes:
        name: Deck name
        description: Deck description
        cards: List of vocabulary cards
        total_cards: Total number of cards
    """

    name: str = Field(..., description="Deck name")
    description: str = Field(..., description="Deck description")
    cards: list[VocabularyCard] = Field(default_factory=list, description="Vocabulary cards")

    @property
    def total_cards(self) -> int:
        """Get total number of cards in deck."""
        return len(self.cards)

    def filter_by_level(self, level: DifficultyLevel) -> list[VocabularyCard]:
        """Filter cards by difficulty level.

        Args:
            level: Difficulty level to filter by

        Returns:
            List of cards matching the level
        """
        return [card for card in self.cards if card.level == level]


class UserProgress(BaseModel):
    """Model for tracking user learning progress.

    Attributes:
        user_id: Unique user identifier
        learned_words: Set of learned word IDs
        review_words: Set of words to review
        total_studied: Total number of words studied
        accuracy_rate: Overall accuracy percentage
    """

    user_id: str = Field(..., description="User ID")
    learned_words: set[str] = Field(default_factory=set, description="Learned words")
    review_words: set[str] = Field(default_factory=set, description="Words to review")
    total_studied: int = Field(default=0, ge=0, description="Total words studied")
    accuracy_rate: float = Field(default=0.0, ge=0.0, le=100.0, description="Accuracy percentage")
